const express = require('express');
const pool    = require('../db');
const { protect, requireAdmin } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

router.use(protect, requireAdmin);

// GET /api/admin/payments
router.get('/payments', async (req, res) => {
  try {
    const { status, search } = req.query;

    let query = `
      SELECT p.id, p.reference_code, p.plan, p.amount, p.currency,
             p.payment_method, p.user_tx_id, p.status,
             p.submitted_at, p.verified_at, p.notes,
             u.id AS user_id, u.email AS user_email,
             u.first_name, u.last_name
      FROM payments p
      JOIN users u ON p.user_id = u.id
      WHERE 1=1
    `;
    const params = [];

    if (status) {
      params.push(status);
      query += ` AND p.status = $${params.length}`;
    }

    if (search) {
      params.push(`%${search}%`);
      query += ` AND (
        p.reference_code ILIKE $${params.length} OR
        u.email ILIKE $${params.length} OR
        p.user_tx_id ILIKE $${params.length} OR
        u.first_name ILIKE $${params.length} OR
        u.last_name ILIKE $${params.length}
      )`;
    }

    query += ' ORDER BY p.submitted_at DESC';

    const result = await pool.query(query, params);
    res.json({ payments: result.rows });

  } catch (err) {
    console.error('Admin payments error:', err.message);
    res.status(500).json({ error: 'Failed to load payments.' });
  }
});

// GET /api/admin/stats
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

// POST /api/admin/verify/:id
router.post('/verify/:id', async (req, res) => {
  try {
    const { id }    = req.params;
    const { notes } = req.body;

    const payment = await pool.query(
      'SELECT p.*, u.email, u.first_name, u.last_name FROM payments p JOIN users u ON p.user_id = u.id WHERE p.id = $1',
      [id]
    );

    if (payment.rows.length === 0) {
      return res.status(404).json({ error: 'Payment not found.' });
    }

    if (payment.rows[0].status === 'verified') {
      return res.status(400).json({ error: 'Payment is already verified.' });
    }

    await pool.query(
      `UPDATE payments
       SET status      = 'verified',
           verified_at = NOW(),
           verified_by = $1,
           notes       = $2
       WHERE id = $3`,
      [req.user.id, notes || null, id]
    );

    const p = payment.rows[0];

    // Send verification email (non-blocking)
    sendVerifiedEmail(p).catch(err =>
      console.error('Verify email error:', err.message)
    );

    res.json({
      message:    `Payment verified. ${p.first_name} now has full access.`,
      payment_id: parseInt(id),
      user_email: p.email
    });

  } catch (err) {
    console.error('Verify payment error:', err.message);
    res.status(500).json({ error: 'Failed to verify payment.' });
  }
});

// POST /api/admin/reject/:id
router.post('/reject/:id', async (req, res) => {
  try {
    const { id }    = req.params;
    const { notes } = req.body;

    const payment = await pool.query(
      'SELECT p.*, u.email, u.first_name FROM payments p JOIN users u ON p.user_id = u.id WHERE p.id = $1',
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

    const p = payment.rows[0];

    // Send rejection email (non-blocking)
    sendRejectedEmail(p, notes).catch(err =>
      console.error('Reject email error:', err.message)
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

// GET /api/admin/users
router.get('/users', async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT u.id, u.email, u.first_name, u.last_name,
             u.is_admin, u.created_at,
             p.status AS payment_status,
             p.plan   AS payment_plan,
             p.amount, p.verified_at,
             p.reference_code, p.user_tx_id,
             p.payment_method
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
    console.error('Admin users error:', err.message);
    res.status(500).json({ error: 'Failed to load users.' });
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

    res.json({ message: 'User access revoked.' });

  } catch (err) {
    console.error('Revoke error:', err.message);
    res.status(500).json({ error: 'Failed to revoke access.' });
  }
});

// ── Email helpers ────────────────────────────────────────
async function sendVerifiedEmail(p) {
  if (!process.env.SMTP_USER) return;
  const nodemailer = require('nodemailer');
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT) || 587,
    secure: false,
    auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS }
  });
  await transporter.sendMail({
    from:    `"DevPath" <${process.env.SMTP_USER}>`,
    to:      p.email,
    subject: '✅ Payment Verified — You Have Full Access!',
    html: `
      <h2>Hi ${p.first_name},</h2>
      <p>Great news! Your payment has been <strong>verified</strong>.</p>
      <p>Your DevPath Full Access account is now <strong>active</strong>.
         You can start learning immediately.</p>
      <p><a href="http://localhost:3000/dashboard.html"
            style="background:#2563eb;color:#fff;padding:10px 24px;
                   border-radius:6px;text-decoration:none;font-weight:bold">
        Go to My Courses →
      </a></p>
      <br><p>— The DevPath Team</p>
    `
  });
}

async function sendRejectedEmail(p, notes) {
  if (!process.env.SMTP_USER) return;
  const nodemailer = require('nodemailer');
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT) || 587,
    secure: false,
    auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS }
  });
  await transporter.sendMail({
    from:    `"DevPath" <${process.env.SMTP_USER}>`,
    to:      p.email,
    subject: '⚠️ Payment Requires Attention — DevPath',
    html: `
      <h2>Hi ${p.first_name},</h2>
      <p>Unfortunately we could not verify your payment.</p>
      ${notes ? `<p><strong>Reason:</strong> ${notes}</p>` : ''}
      <p>Please contact us or try submitting your payment again with the correct transaction details.</p>
      <p><a href="http://localhost:3000/submit-payment.html">Try Again →</a></p>
      <br><p>— The DevPath Team</p>
    `
  });
}

module.exports = router;
