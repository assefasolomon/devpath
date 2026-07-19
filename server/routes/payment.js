const express = require('express');
const pool    = require('../db');
const { protect } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

const PLANS = {
  pro: { name: 'DevPath Full Access', amount: 599 }
};

function generateRefCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = 'PAY-';
  for (let i = 0; i < 5; i++) {
    code += chars[Math.floor(Math.random() * chars.length)];
  }
  return code;
}

function accountDetails() {
  return {
    telebirr_number: process.env.TELEBIRR_NUMBER,
    telebirr_name:   process.env.TELEBIRR_NAME,
    cbe_account:     process.env.CBE_ACCOUNT,
    cbe_name:        process.env.CBE_NAME,
  };
}

// GET /api/payment/info
router.get('/info', protect, async (req, res) => {
  try {
    const existing = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (existing.rows.length > 0) {
      const p = existing.rows[0];
      return res.json({
        has_payment:    true,
        status:         p.status,
        plan:           p.plan,
        amount:         p.amount,
        reference_code: p.reference_code,
        submitted_at:   p.submitted_at,
        user_tx_id:     p.user_tx_id,
        payment_method: p.payment_method,
        ...accountDetails()
      });
    }

    res.json({
      has_payment: false,
      plans:       PLANS,
      ...accountDetails()
    });

  } catch (err) {
    console.error('Payment info error:', err.message);
    res.status(500).json({ error: 'Failed to load payment info.' });
  }
});

// POST /api/payment/generate-reference
router.post('/generate-reference', protect, async (req, res) => {
  try {
    const { plan } = req.body;

    if (!PLANS[plan]) {
      return res.status(400).json({ error: 'Invalid plan selected.' });
    }

    const verified = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1 AND status = 'verified'`,
      [req.user.id]
    );
    if (verified.rows.length > 0) {
      return res.status(400).json({
        error: 'You already have an active verified payment.'
      });
    }

    const existing = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1 AND status = 'pending'`,
      [req.user.id]
    );
    if (existing.rows.length > 0) {
      const p = existing.rows[0];
      return res.json({
        reference_code: p.reference_code,
        plan:           p.plan,
        plan_name:      PLANS[p.plan]?.name || p.plan,
        amount:         p.amount,
        currency:       'ETB',
        ...accountDetails()
      });
    }

    let reference_code;
    let unique = false;
    while (!unique) {
      reference_code = generateRefCode();
      const check = await pool.query(
        'SELECT id FROM payments WHERE reference_code = $1',
        [reference_code]
      );
      if (check.rows.length === 0) unique = true;
    }

    const selectedPlan = PLANS[plan];

    await pool.query(
      `INSERT INTO payments
        (user_id, plan, amount, currency, reference_code, status)
       VALUES ($1, $2, $3, 'ETB', $4, 'pending')`,
      [req.user.id, plan, selectedPlan.amount, reference_code]
    );

    res.json({
      reference_code,
      plan:      plan,
      plan_name: selectedPlan.name,
      amount:    selectedPlan.amount,
      currency:  'ETB',
      ...accountDetails()
    });

  } catch (err) {
    console.error('Generate reference error:', err.message);
    res.status(500).json({ error: 'Failed to generate reference code.' });
  }
});

// POST /api/payment/submit
router.post('/submit', protect, async (req, res) => {
  try {
    const { reference_code, user_tx_id, payment_method } = req.body;

    if (!reference_code || !user_tx_id || !payment_method) {
      return res.status(400).json({
        error: 'Reference code, transaction ID, and payment method are required.'
      });
    }

    const validMethods = ['telebirr', 'cbe', 'awash', 'bank_transfer'];
    if (!validMethods.includes(payment_method)) {
      return res.status(400).json({ error: 'Invalid payment method.' });
    }

    const result = await pool.query(
      `SELECT * FROM payments
       WHERE reference_code = $1 AND user_id = $2`,
      [reference_code.toUpperCase().trim(), req.user.id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        error: 'Reference code not found. Please check and try again.'
      });
    }

    const payment = result.rows[0];

    if (payment.status === 'verified') {
      return res.status(400).json({
        error: 'This payment is already verified. You have full access.'
      });
    }

    if (payment.status === 'rejected') {
      return res.status(400).json({
        error: 'This payment was rejected. Please contact support.'
      });
    }

    if (payment.user_tx_id) {
      return res.status(400).json({
        error: 'You have already submitted this payment. Please wait for verification.'
      });
    }

    await pool.query(
      `UPDATE payments
       SET user_tx_id     = $1,
           payment_method = $2,
           submitted_at   = NOW()
       WHERE id = $3`,
      [user_tx_id.trim(), payment_method, payment.id]
    );

    // Send email notification (non-blocking)
    sendPaymentSubmittedEmail(req.user, payment.reference_code, payment.amount)
      .catch(err => console.error('Email error:', err.message));

    res.json({
      message:        'Payment submitted successfully.',
      status:         'pending',
      reference_code: payment.reference_code
    });

  } catch (err) {
    console.error('Submit payment error:', err.message);
    res.status(500).json({ error: 'Failed to submit payment. Please try again.' });
  }
});

// GET /api/payment/status
router.get('/status', protect, async (req, res) => {
  try {
    const result = await pool.query(
      `SELECT id, plan, amount, currency, reference_code,
              payment_method, status, submitted_at, verified_at, user_tx_id
       FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (result.rows.length === 0) {
      return res.json({ status: 'none' });
    }

    res.json(result.rows[0]);

  } catch (err) {
    console.error('Payment status error:', err.message);
    res.status(500).json({ error: 'Failed to get payment status.' });
  }
});

// GET /api/payment/check-access
router.get('/check-access', protect, async (req, res) => {
  try {
    if (req.user.is_admin) {
      return res.json({ has_access: true, reason: 'admin' });
    }

    const result = await pool.query(
      `SELECT status FROM payments
       WHERE user_id = $1 AND status = 'verified'
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (result.rows.length > 0) {
      return res.json({ has_access: true, reason: 'verified' });
    }

    const pending = await pool.query(
      `SELECT status FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    res.json({
      has_access: false,
      reason:     pending.rows[0]?.status || 'none'
    });

  } catch (err) {
    console.error('Check access error:', err.message);
    res.status(500).json({ error: 'Failed to check access.' });
  }
});

// ── Email helpers (using nodemailer if configured) ───────
async function sendPaymentSubmittedEmail(user, refCode, amount) {
  if (!process.env.SMTP_USER) return; // skip if not configured
  const nodemailer = require('nodemailer');
  const transporter = nodemailer.createTransport({
    host:   process.env.SMTP_HOST,
    port:   parseInt(process.env.SMTP_PORT) || 587,
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });
  await transporter.sendMail({
    from:    `"DevPath" <${process.env.SMTP_USER}>`,
    to:      user.email,
    subject: 'Payment Received — DevPath',
    html: `
      <h2>Hi ${user.first_name},</h2>
      <p>We have received your payment submission for <strong>DevPath Full Access</strong>.</p>
      <p><strong>Reference Code:</strong> ${refCode}<br>
         <strong>Amount:</strong> ${amount} ETB</p>
      <p>We will verify your transfer within <strong>1–2 hours</strong> during business hours (8am–8pm).</p>
      <p>Once verified, you will have immediate access to all courses.</p>
      <br><p>— The DevPath Team</p>
    `
  });
}

module.exports = router;

