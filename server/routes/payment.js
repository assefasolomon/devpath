const express = require('express');
const pool    = require('../db');
const { protect } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

// ── HELPER: generate unique reference code ───────────────
// Generates codes like PAY-8F3K2
function generateRefCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = 'PAY-';
  for (let i = 0; i < 5; i++) {
    code += chars[Math.floor(Math.random() * chars.length)];
  }
  return code;
}

// ── HELPER: plan prices ──────────────────────────────────
const PLAN = {
 
  pro:     { name: 'Pro',      amount: 599  },  // ~$149 in ETB
  
};

// ────────────────────────────────────────────────────────
// GET /api/payment/info
// Returns payment instructions for the user
// ────────────────────────────────────────────────────────
router.get('/info', protect, async (req, res) => {
  try {
    // Check if user already has a pending or verified payment
    const existing = await pool.query(
      `SELECT * FROM payments
       WHERE user_id = $1
       ORDER BY submitted_at DESC
       LIMIT 1`,
      [req.user.id]
    );

    if (existing.rows.length > 0) {
      const p = existing.rows[0];
      return res.json({
        has_payment: true,
        status:         p.status,
        plan:           p.plan,
        amount:         p.amount,
        reference_code: p.reference_code,
        submitted_at:   p.submitted_at
      });
    }

    res.json({
      has_payment: false,
      telebirr_number: process.env.TELEBIRR_NUMBER,
      telebirr_name:   process.env.TELEBIRR_NAME,
      cbe_account:     process.env.CBE_ACCOUNT,
      cbe_name:        process.env.CBE_NAME,
      plans:           PLANS
    });

  } catch (err) {
    console.error('Payment info error:', err.message);
    res.status(500).json({ error: 'Failed to load payment info.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/payment/generate-reference
// Generates a unique reference code for the user
// Called when user selects a plan
// ────────────────────────────────────────────────────────
router.post('/generate-reference', protect, async (req, res) => {
  try {
    const { plan } = req.body;

    if (!PLANS[plan]) {
      return res.status(400).json({ error: 'Invalid plan selected.' });
    }

    // Check if user already has a pending payment
    const existing = await pool.query(
      `SELECT * FROM payments
       WHERE user_id = $1
       AND status = 'pending'`,
      [req.user.id]
    );

    if (existing.rows.length > 0) {
      // Return existing reference code
      return res.json({
        reference_code:  existing.rows[0].reference_code,
        plan:            existing.rows[0].plan,
        amount:          existing.rows[0].amount,
        telebirr_number: process.env.TELEBIRR_NUMBER,
        telebirr_name:   process.env.TELEBIRR_NAME,
        cbe_account:     process.env.CBE_ACCOUNT,
        cbe_name:        process.env.CBE_NAME,
      });
    }

    // Check if already verified
    const verified = await pool.query(
      `SELECT * FROM payments
       WHERE user_id = $1
       AND status = 'verified'`,
      [req.user.id]
    );

    if (verified.rows.length > 0) {
      return res.status(400).json({
        error: 'You already have an active verified payment.'
      });
    }

    // Generate unique reference code
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

    // Create pending payment row
    await pool.query(
      `INSERT INTO payments
        (user_id, plan, amount, currency, reference_code, status)
       VALUES ($1, $2, $3, 'ETB', $4, 'pending')`,
      [req.user.id, plan, selectedPlan.amount, reference_code]
    );

    res.json({
      reference_code,
      plan:            plan,
      plan_name:       selectedPlan.name,
      amount:          selectedPlan.amount,
      currency:        'ETB',
      telebirr_number: process.env.TELEBIRR_NUMBER,
      telebirr_name:   process.env.TELEBIRR_NAME,
      cbe_account:     process.env.CBE_ACCOUNT,
      cbe_name:        process.env.CBE_NAME,
    });

  } catch (err) {
    console.error('Generate reference error:', err.message);
    res.status(500).json({ error: 'Failed to generate reference code.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/payment/submit
// User submits their transaction ID after paying
// ────────────────────────────────────────────────────────
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

    // Find the payment row
    const result = await pool.query(
      `SELECT * FROM payments
       WHERE reference_code = $1
       AND user_id = $2`,
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
        error: 'This payment was rejected. Please contact support or start a new payment.'
      });
    }

    // Update payment with transaction details
    await pool.query(
      `UPDATE payments
       SET user_tx_id = $1,
           payment_method = $2,
           submitted_at = NOW()
       WHERE id = $3`,
      [user_tx_id.trim(), payment_method, payment.id]
    );

    res.json({
      message: 'Payment submitted successfully. We will verify it within 1-2 hours and send you an email confirmation.',
      status: 'pending',
      reference_code: payment.reference_code
    });

  } catch (err) {
    console.error('Submit payment error:', err.message);
    res.status(500).json({ error: 'Failed to submit payment. Please try again.' });
  }
});

// ────────────────────────────────────────────────────────
// GET /api/payment/status
// Returns the current payment status for logged in user
// ────────────────────────────────────────────────────────
router.get('/status', protect, async (req, res) => {
  try {
    const result = await pool.query(
      `SELECT id, plan, amount, currency, reference_code,
              payment_method, status, submitted_at, verified_at
       FROM payments
       WHERE user_id = $1
       ORDER BY submitted_at DESC
       LIMIT 1`,
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

module.exports = router;
