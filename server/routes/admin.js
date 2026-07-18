const express = require('express');
const pool    = require('../db');
const { protect, requireAdmin } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

// All admin routes require login + admin status
router.use(protect, requireAdmin);

// ────────────────────────────────────────────────────────
// GET /api/admin/payments
// Returns all payments with user details
// ────────────────────────────────────────────────────────
router.get('/payments', async (req, res) => {
  try {
    const { status } = req.query;

    let query = `
      SELECT
        p.id,
        p.reference_code,
        p.plan,
        p.amount,
        p.currency,
        p.payment_method,
        p.user_tx_id,
        p.status,
        p.submitted_at,
        p.verified_at,
        p.notes,
        u.id        AS user_id,
        u.email     AS user_email,
        u.first_name,
        u.last_name
      FROM payments p
      JOIN users u ON p.user_id = u.id
    `;

    const params = [];
    if (status) {
      query += ' WHERE p.status = $1';
      params.push(status);
    }

    query += ' ORDER BY p.submitted_at DESC';

    const result = await pool.query(query, params);
    res.json({ payments: result.rows });

  } catch (err) {
    console.error('Admin payments error:', err.message);
    res.status(500).json({ error: 'Failed to load payments.' });
  }
});

// ────────────────────────────────────────────────────────
// GET /api/admin/stats
// Returns dashboard statistics
// ────────────────────────────────────────────────────────
router.get('/stats', async (req, res) => {
  try {
    const stats = await pool.query(`
      SELECT
        COUNT(*) FILTER (WHERE status = 'pending')  AS pending,
        COUNT(*) FILTER (WHERE status = 'verified') AS verified,
        COUNT(*) FILTER (WHERE status = 'rejected') AS rejected,
        SUM(amount) FILTER (WHERE status = 'verified') AS total_revenue
      FROM payments
    `);

    const users = await pool.query(
      'SELECT COUNT(*) AS total_users FROM users WHERE is_admin = FALSE'
    );

    res.json({
      pending:       parseInt(stats.rows[0].pending),
      verified:      parseInt(stats.rows[0].verified),
      rejected:      parseInt(stats.rows[0].rejected),
      total_revenue: parseFloat(stats.rows[0].total_revenue) || 0,
      total_users:   parseInt(users.rows[0].total_users)
    });

  } catch (err) {
    console.error('Admin stats error:', err.message);
    res.status(500).json({ error: 'Failed to load stats.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/admin/verify/:id
// Verify a payment — unlocks user access
// ────────────────────────────────────────────────────────
router.post('/verify/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { notes } = req.body;

    // Find the payment
    const payment = await pool.query(
      'SELECT * FROM payments WHERE id = $1',
      [id]
    );

    if (payment.rows.length === 0) {
      return res.status(404).json({ error: 'Payment not found.' });
    }

    if (payment.rows[0].status === 'verified') {
      return res.status(400).json({ error: 'Payment is already verified.' });
    }

    // Update status to verified
    await pool.query(
      `UPDATE payments
       SET status      = 'verified',
           verified_at = NOW(),
           verified_by = $1,
           notes       = $2
       WHERE id = $3`,
      [req.user.id, notes || null, id]
    );

    // Get user details for response
    const user = await pool.query(
      'SELECT email, first_name FROM users WHERE id = $1',
      [payment.rows[0].user_id]
    );

    res.json({
      message:  `Payment verified. ${user.rows[0].first_name} now has full access.`,
      payment_id: parseInt(id),
      user_email: user.rows[0].email
    });

  } catch (err) {
    console.error('Verify payment error:', err.message);
    res.status(500).json({ error: 'Failed to verify payment.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/admin/reject/:id
// Reject a payment
// ────────────────────────────────────────────────────────
router.post('/reject/:id', async (req, res) => {
  try {
    const { id }    = req.params;
    const { notes } = req.body;

    const payment = await pool.query(
      'SELECT * FROM payments WHERE id = $1',
      [id]
    );

    if (payment.rows.length === 0) {
      return res.status(404).json({ error: 'Payment not found.' });
    }

    if (payment.rows[0].status === 'verified') {
      return res.status(400).json({
        error: 'Cannot reject an already verified payment.'
      });
    }

    await pool.query(
      `UPDATE payments
       SET status      = 'rejected',
           verified_by = $1,
           notes       = $2
       WHERE id = $3`,
      [req.user.id, notes || 'Rejected by admin', id]
    );

    res.json({
      message:    'Payment rejected.',
      payment_id: parseInt(id)
    });

  } catch (err) {
    console.error('Reject payment error:', err.message);
    res.status(500).json({ error: 'Failed to reject payment.' });
  }
});

// ────────────────────────────────────────────────────────
// GET /api/admin/users
// Returns all users
// ────────────────────────────────────────────────────────
router.get('/users', async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT
        u.id,
        u.email,
        u.first_name,
        u.last_name,
        u.is_admin,
        u.created_at,
        p.status        AS payment_status,
        p.plan          AS payment_plan,
        p.verified_at
      FROM users u
      LEFT JOIN payments p ON p.user_id = u.id
        AND p.id = (
          SELECT id FROM payments
          WHERE user_id = u.id
          ORDER BY submitted_at DESC
          LIMIT 1
        )
      WHERE u.is_admin = FALSE
      ORDER BY u.created_at DESC
    `);

    res.json({ users: result.rows });

  } catch (err) {
    console.error('Admin users error:', err.message);
    res.status(500).json({ error: 'Failed to load users.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/admin/revoke/:userId
// Revoke access from a user
// ────────────────────────────────────────────────────────
router.post('/revoke/:userId', async (req, res) => {
  try {
    const { userId } = req.params;
    const { notes  } = req.body;

    await pool.query(
      `UPDATE payments
       SET status = 'rejected',
           notes  = $1
       WHERE user_id = $2
       AND status = 'verified'`,
      [notes || 'Access revoked by admin', userId]
    );

    res.json({ message: 'User access revoked.' });

  } catch (err) {
    console.error('Revoke error:', err.message);
    res.status(500).json({ error: 'Failed to revoke access.' });
  }
});

module.exports = router;
