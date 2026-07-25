const express = require('express');
const pool    = require('../db');
const { protect } = require('../middleware/protect');
require('dotenv').config();

const router = express.Router();

// ── Plan ─────────────────────────────────────────────────
const PLAN = {
  id:       'pro',
  name:     'Freelance Skills Hub Full Access',
  amount:   599,
  currency: 'ETB'
};

// ── Account details ───────────────────────────────────────
function getAccountDetails() {
  return {
    telebirr_number: process.env.TELEBIRR_NUMBER || null,
    telebirr_name:   process.env.TELEBIRR_NAME   || null,
    cbe_account:     process.env.CBE_ACCOUNT      || null,
    cbe_name:        process.env.CBE_NAME         || null,
  };
}

// ── Reference code generator ──────────────────────────────
function generateRefCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = 'PAY-';
  for (let i = 0; i < 5; i++) {
    code += chars[Math.floor(Math.random() * chars.length)];
  }
  return code;
}

// ────────────────────────────────────────────────────────
// GET /api/payment/details
// ────────────────────────────────────────────────────────
router.get('/details', protect, async (req, res) => {
  try {
    const accounts = getAccountDetails();

    const verified = await pool.query(
      `SELECT id FROM payments WHERE user_id = $1 AND status = 'verified'`,
      [req.user.id]
    );
    if (verified.rows.length > 0) {
      return res.json({ already_paid: true, status: 'verified', ...accounts });
    }

    res.json({ already_paid: false, plan: PLAN, ...accounts });

  } catch (err) {
    console.error('Payment details error:', err.message);
    res.status(500).json({ error: 'Failed to load payment details.' });
  }
});

// ────────────────────────────────────────────────────────
// GET /api/payment/info
// ────────────────────────────────────────────────────────
router.get('/info', protect, async (req, res) => {
  try {
    const accounts = getAccountDetails();

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
        ...accounts
      });
    }

    res.json({ has_payment: false, plan: PLAN, ...accounts });

  } catch (err) {
    console.error('Payment info error:', err.message);
    res.status(500).json({ error: 'Failed to load payment info.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/payment/initialize
// ────────────────────────────────────────────────────────
router.post('/initialize', protect, async (req, res) => {
  try {
    const accounts = getAccountDetails();

    // Already verified
    const verified = await pool.query(
      `SELECT id FROM payments WHERE user_id = $1 AND status = 'verified'`,
      [req.user.id]
    );
    if (verified.rows.length > 0) {
      return res.status(400).json({ error: 'You already have full access.' });
    }

    // Return existing pending
    const pending = await pool.query(
      `SELECT * FROM payments WHERE user_id = $1 AND status = 'pending'`,
      [req.user.id]
    );
    if (pending.rows.length > 0) {
      const p = pending.rows[0];
      return res.json({
        reference_code:  p.reference_code,
        plan_name:       PLAN.name,
        amount:          p.amount,
        currency:        PLAN.currency,
        already_pending: true,
        has_tx_id:       !!p.user_tx_id,
        ...accounts
      });
    }

    // Delete rejected so user can start fresh
    await pool.query(
      `DELETE FROM payments WHERE user_id = $1 AND status = 'rejected'`,
      [req.user.id]
    );

    // Generate unique reference code
    let reference_code = null;
    for (let i = 0; i < 10; i++) {
      const candidate = generateRefCode();
      const check = await pool.query(
        'SELECT id FROM payments WHERE reference_code = $1',
        [candidate]
      );
      if (check.rows.length === 0) {
        reference_code = candidate;
        break;
      }
    }

    if (!reference_code) {
      return res.status(500).json({ error: 'Failed to generate reference code.' });
    }

    // Create payment record
    await pool.query(
      `INSERT INTO payments (user_id, plan, amount, currency, reference_code, status)
       VALUES ($1, $2, $3, $4, $5, 'pending')`,
      [req.user.id, PLAN.id, PLAN.amount, PLAN.currency, reference_code]
    );

    res.json({
      reference_code,
      plan_name:       PLAN.name,
      amount:          PLAN.amount,
      currency:        PLAN.currency,
      already_pending: false,
      has_tx_id:       false,
      ...accounts
    });

  } catch (err) {
    console.error('Initialize payment error:', err.message);
    res.status(500).json({ error: 'Failed to initialize payment.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/payment/submit
// ────────────────────────────────────────────────────────
router.post('/submit', protect, async (req, res) => {
  try {
    const { reference_code, user_tx_id, payment_method, notes } = req.body;

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

    const result = await pool.query(
      `SELECT * FROM payments
       WHERE reference_code = $1 AND user_id = $2`,
      [reference_code.toUpperCase().trim(), req.user.id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        error: 'Reference code not found. Please use the code we generated for you.'
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
        error: 'This payment was rejected. Please start a new payment.'
      });
    }
    if (payment.user_tx_id) {
      return res.status(400).json({
        error: 'You already submitted payment details. Please wait for verification.'
      });
    }

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

    // Send email notification non-blocking
    try {
      const emailModule = require('../email');
      emailModule.sendPaymentSubmittedEmail(req.user, updated.rows[0]).catch(() => {});
    } catch (e) {}

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

// ────────────────────────────────────────────────────────
// GET /api/payment/status
// ────────────────────────────────────────────────────────
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

// ────────────────────────────────────────────────────────
// GET /api/payment/check-access
// ────────────────────────────────────────────────────────
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

module.exports = router;
