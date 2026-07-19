const express = require('express');
const pool    = require('../db');
const email   = require('../email');
const { protect } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

const PLAN = {
  id:     'pro',
  name:   'DevPath Full Access',
  amount: 599,
  currency: 'ETB'
};

function getAccountDetails() {
  return {
    telebirr_number: process.env.TELEBIRR_NUMBER  || 'Not configured',
    telebirr_name:   process.env.TELEBIRR_NAME    || 'Not configured',
    cbe_account:     process.env.CBE_ACCOUNT      || 'Not configured',
    cbe_name:        process.env.CBE_NAME         || 'Not configured',
  };
}

function generateRefCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = 'PAY-';
  for (let i = 0; i < 5; i++) {
    code += chars[Math.floor(Math.random() * chars.length)];
  }
  return code;
}

// GET /api/payment/details
// Returns plan + account details — used by pay.html on load
router.get('/details', protect, async (req, res) => {
  try {
    const accounts = getAccountDetails();

    // Check if user already has a payment
    const existing = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (existing.rows.length > 0 && existing.rows[0].status === 'verified') {
      return res.json({
        already_paid: true,
        status: 'verified',
        ...accounts
      });
    }

    res.json({
      already_paid: false,
      plan: PLAN,
      ...accounts
    });

  } catch (err) {
    console.error('Payment details error:', err.message);
    res.status(500).json({ error: 'Failed to load payment details.' });
  }
});

// POST /api/payment/initialize
// Called when user clicks "Get Full Access" — generates reference code
router.post('/initialize', protect, async (req, res) => {
  try {
    // Check if already verified
    const verified = await pool.query(
      `SELECT id FROM payments WHERE user_id = $1 AND status = 'verified'`,
      [req.user.id]
    );
    if (verified.rows.length > 0) {
      return res.status(400).json({ error: 'You already have full access.' });
    }

    // Check if already has a pending payment — return existing reference
    const pending = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1 AND status = 'pending'`,
      [req.user.id]
    );
    if (pending.rows.length > 0) {
      const p = pending.rows[0];
      return res.json({
        reference_code: p.reference_code,
        plan_name:      PLAN.name,
        amount:         p.amount,
        currency:       PLAN.currency,
        already_pending: true,
        has_tx_id:      !!p.user_tx_id,
        ...getAccountDetails()
      });
    }

    // Check for rejected — delete it so user can start fresh
    await pool.query(
      `DELETE FROM payments WHERE user_id = $1 AND status = 'rejected'`,
      [req.user.id]
    );

    // Generate unique reference code
    let reference_code;
    let attempts = 0;
    while (attempts < 10) {
      const candidate = generateRefCode();
      const check = await pool.query(
        'SELECT id FROM payments WHERE reference_code = $1',
        [candidate]
      );
      if (check.rows.length === 0) {
        reference_code = candidate;
        break;
      }
      attempts++;
    }

    if (!reference_code) {
      return res.status(500).json({ error: 'Failed to generate reference code.' });
    }

    // Insert pending payment
    await pool.query(
      `INSERT INTO payments (user_id, plan, amount, currency, reference_code, status)
       VALUES ($1, $2, $3, $4, $5, 'pending')`,
      [req.user.id, PLAN.id, PLAN.amount, PLAN.currency, reference_code]
    );

    res.json({
      reference_code,
      plan_name:  PLAN.name,
      amount:     PLAN.amount,
      currency:   PLAN.currency,
      already_pending: false,
      has_tx_id:  false,
      ...getAccountDetails()
    });

  } catch (err) {
    console.error('Initialize payment error:', err.message);
    res.status(500).json({ error: 'Failed to initialize payment.' });
  }
});

// POST /api/payment/submit
// Called when user submits their transaction details
router.post('/submit', protect, async (req, res) => {
  try {
    const { reference_code, user_tx_id, payment_method, notes } = req.body;

    // Validate
    if (!reference_code?.trim()) {
      return res.status(400).json({ error: 'Reference code is required.' });
    }
    if (!user_tx_id?.trim()) {
      return res.status(400).json({ error: 'Transaction ID is required.' });
    }
    if (!payment_method) {
      return res.status(400).json({ error: 'Payment method is required.' });
    }

    const validMethods = ['telebirr', 'cbe', 'awash', 'bank_transfer'];
    if (!validMethods.includes(payment_method)) {
      return res.status(400).json({ error: 'Invalid payment method.' });
    }

    // Find payment
    const result = await pool.query(
      `SELECT * FROM payments
       WHERE reference_code = $1 AND user_id = $2`,
      [reference_code.toUpperCase().trim(), req.user.id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        error: 'Reference code not found. Please go back and use the code we generated for you.'
      });
    }

    const payment = result.rows[0];

    if (payment.status === 'verified') {
      return res.status(400).json({
        error: 'This payment is already verified. You have full access to all courses.'
      });
    }

    if (payment.status === 'rejected') {
      return res.status(400).json({
        error: 'This payment was rejected. Please start a new payment.'
      });
    }

    if (payment.user_tx_id) {
      return res.status(400).json({
        error: 'You have already submitted transaction details for this payment. Please wait for verification.'
      });
    }

    // Update payment with transaction details
    const updated = await pool.query(
      `UPDATE payments
       SET user_tx_id     = $1,
           payment_method = $2,
           notes          = $3,
           submitted_at   = NOW()
       WHERE id = $4
       RETURNING *`,
      [user_tx_id.trim(), payment_method, notes?.trim() || null, payment.id]
    );

    // Send email notification (non-blocking)
    email.sendPaymentSubmittedEmail(req.user, updated.rows[0]).catch(() => {});

    res.json({
      message:        'Payment submitted successfully.',
      status:         'pending',
      reference_code: payment.reference_code,
      amount:         payment.amount,
      currency:       PLAN.currency,
      user_tx_id:     user_tx_id.trim(),
      payment_method,
      submitted_at:   updated.rows[0].submitted_at
    });

  } catch (err) {
    console.error('Submit payment error:', err.message);
    res.status(500).json({ error: 'Failed to submit payment. Please try again.' });
  }
});

// GET /api/payment/status
// Full payment status — used by dashboard and status page
router.get('/status', protect, async (req, res) => {
  try {
    const result = await pool.query(
      `SELECT id, plan, amount, currency, reference_code,
              payment_method, user_tx_id, status,
              submitted_at, verified_at, notes
       FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (result.rows.length === 0) {
      return res.json({ status: 'none' });
    }

    const p = result.rows[0];
    res.json({
      id:             p.id,
      plan:           p.plan,
      plan_name:      PLAN.name,
      amount:         p.amount,
      currency:       p.currency,
      reference_code: p.reference_code,
      payment_method: p.payment_method,
      user_tx_id:     p.user_tx_id,
      status:         p.status,
      submitted_at:   p.submitted_at,
      verified_at:    p.verified_at,
      notes:          p.notes
    });

  } catch (err) {
    console.error('Payment status error:', err.message);
    res.status(500).json({ error: 'Failed to get payment status.' });
  }
});

module.exports = router;
