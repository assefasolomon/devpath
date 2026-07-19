const express = require('express');
const pool    = require('../db');
const email   = require('../email');
const { protect, requireAdmin } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();
router.use(protect, requireAdmin);

// GET /api/admin/stats
router.get('/stats', async (req, res) => {
  try {
    const stats = await pool.query(`
      SELECT
        COUNT(*) FILTER (WHERE status = 'pending')  AS pending,
        COUNT(*) FILTER (WHERE status = 'verified') AS verified,
        COUNT(*) FILTER (WHERE status = 'rejected') AS rejected,
        COALESCE(SUM(amount) FILTER (WHERE status = 'verified'), 0) AS total_revenue
      FROM payments
    `);
    const users = await pool.query(
      `SELECT COUNT(*) AS total FROM users WHERE is_admin = FALSE`
    );
    const s = stats.rows[0];
    res.json({
      pending:       parseInt(s.pending),
      verified:      parseInt(s.verified),
      rejected:      parseInt(s.rejected),
      total_revenue: parseFloat(s.total_revenue),
      total_users:   parseInt(users.rows[0].total)
    });
  } catch (err) {
    console.error('Stats error:', err.message);
    res.status(500).json({ error: 'Failed to load stats.' });
  }
});

// GET /api/admin/payments?status=pending&search=xxx
router.get('/payments', async (req, res) => {
  try {
    const { status, search } = req.query;
    const params = [];
    let where = 'WHERE 1=1';

    if (status) {
      params.push(status);
      where += ` AND p.status = $${params.length}`;
    }
    if (search?.trim()) {
      params.push(`%${search.trim()}%`);
      const n = params.length;
      where += ` AND (
        p.reference_code ILIKE $${n} OR
        p.user_tx_id     ILIKE $${n} OR
        u.email          ILIKE $${n} OR
        u.first_name     ILIKE $${n} OR
        u.last_name      ILIKE $${n}
      )`;
    }

    const result = await pool.query(`
      SELECT
        p.id, p.reference_code, p.plan, p.amount, p.currency,
        p.payment_method, p.user_tx_id, p.status,
        p.submitted_at, p.verified_at, p.notes,
        u.id         AS user_id,
        u.email      AS user_email,
        u.first_name, u.last_name
      FROM payments p
      JOIN users u ON p.user_id = u.id
      ${where}
      ORDER BY p.submitted_at DESC
    `, params);

    res.json({ payments: result.rows, total: result.rows.length });
  } catch (err) {
    console.error('Payments error:', err.message);
    res.status(500).json({ error: 'Failed to load payments.' });
  }
});

// GET /api/admin/users
router.get('/users', async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT
        u.id, u.email, u.first_name, u.last_name, u.created_at,
        p.status         AS payment_status,
        p.plan           AS payment_plan,
        p.amount, p.reference_code,
        p.user_tx_id, p.payment_method,
        p.submitted_at, p.verified_at
      FROM users u
      LEFT JOIN payments p ON p.user_id = u.id
        AND p.id = (
          SELECT id FROM payments WHERE user_id = u.id
          ORDER BY submitted_at DESC LIMIT 1
        )
      WHERE u.is_admin = FALSE
      ORDER BY u.created_at DESC
    `);
    res.json({ users: result.rows });
  } catch (err) {
    console.error('Users error:', err.message);
    res.status(500).json({ error: 'Failed to load users.' });
  }
});

// POST /api/admin/verify/:id
router.post('/verify/:id', async (req, res) => {
  try {
    const { id }    = req.params;
    const { notes } = req.body;

    // Get payment with user info
    const pResult = await pool.query(
      `SELECT p.*, u.email, u.first_name, u.last_name
       FROM payments p JOIN users u ON p.user_id = u.id
       WHERE p.id = $1`,
      [id]
    );

    if (pResult.rows.length === 0) {
      return res.status(404).json({ error: 'Payment not found.' });
    }

    const p = pResult.rows[0];

    if (p.status === 'verified') {
      return res.status(400).json({ error: 'Payment is already verified.' });
    }

    if (!p.user_tx_id) {
      return res.status(400).json({
        error: 'Cannot verify — user has not submitted transaction details yet.'
      });
    }

    // Verify payment
    await pool.query(
      `UPDATE payments
       SET status      = 'verified',
           verified_at = NOW(),
           verified_by = $1,
           notes       = COALESCE($2, notes)
       WHERE id = $3`,
      [req.user.id, notes || null, id]
    );

    // Send verification email (non-blocking)
    const user    = { email: p.email, first_name: p.first_name };
    const payment = { amount: p.amount, reference_code: p.reference_code };
    email.sendPaymentVerifiedEmail(user, payment).catch(() => {});

    res.json({
      message:    `✅ Payment verified. ${p.first_name} ${p.last_name} now has full access.`,
      payment_id: parseInt(id),
      user_email: p.email
    });

  } catch (err) {
    console.error('Verify error:', err.message);
    res.status(500).json({ error: 'Failed to verify payment.' });
  }
});

// POST /api/admin/reject/:id
router.post('/reject/:id', async (req, res) => {
  try {
    const { id }    = req.params;
    const { notes } = req.body;

    if (!notes?.trim()) {
      return res.status(400).json({ error: 'Rejection reason is required.' });
    }

    const pResult = await pool.query(
      `SELECT p.*, u.email, u.first_name
       FROM payments p JOIN users u ON p.user_id = u.id
       WHERE p.id = $1`,
      [id]
    );

    if (pResult.rows.length === 0) {
      return res.status(404).json({ error: 'Payment not found.' });
    }

    const p = pResult.rows[0];

    if (p.status === 'verified') {
      return res.status(400).json({ error: 'Cannot reject a verified payment.' });
    }

    await pool.query(
      `UPDATE payments
       SET status      = 'rejected',
           verified_by = $1,
           notes       = $2,
           verified_at = NOW()
       WHERE id = $3`,
      [req.user.id, notes.trim(), id]
    );

    // Send rejection email (non-blocking)
    const user    = { email: p.email, first_name: p.first_name };
    const payment = { reference_code: p.reference_code };
    email.sendPaymentRejectedEmail(user, payment, notes.trim()).catch(() => {});

    res.json({ message: 'Payment rejected.', payment_id: parseInt(id) });

  } catch (err) {
    console.error('Reject error:', err.message);
    res.status(500).json({ error: 'Failed to reject payment.' });
  }
});

// POST /api/admin/revoke/:userId
router.post('/revoke/:userId', async (req, res) => {
  try {
    const { userId } = req.params;
    const { notes  } = req.body;

    await pool.query(
      `UPDATE payments SET status = 'rejected', notes = $1
       WHERE user_id = $2 AND status = 'verified'`,
      [notes || 'Access revoked by admin', userId]
    );

    res.json({ message: 'Access revoked.' });
  } catch (err) {
    console.error('Revoke error:', err.message);
    res.status(500).json({ error: 'Failed to revoke access.' });
  }
});

module.exports = router;
