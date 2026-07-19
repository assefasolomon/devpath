const express = require('express');
const bcrypt  = require('bcryptjs');
const jwt     = require('jsonwebtoken');
const pool    = require('../db');
require('dotenv').config();

const router = express.Router();

// ── HELPER: generate JWT ─────────────────────────────────
function generateToken(userId) {
  return jwt.sign(
    { userId },
    process.env.JWT_SECRET,
    { expiresIn: '30d' }
  );
}

// ── HELPER: set cookie ───────────────────────────────────
function setTokenCookie(res, token) {
  res.cookie('devpath_token', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge: 30 * 24 * 60 * 60 * 1000 // 30 days
  });
}

// ────────────────────────────────────────────────────────
// POST /api/auth/register
// ────────────────────────────────────────────────────────
router.post('/register', async (req, res) => {
  try {
    const { first_name, last_name, email, password } = req.body;

    // Validate fields
    if (!first_name || !last_name || !email || !password) {
      return res.status(400).json({ error: 'All fields are required.' });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: 'Password must be at least 6 characters.' });
    }

    // Check if email already exists
    const existing = await pool.query(
      'SELECT id FROM users WHERE email = $1',
      [email.toLowerCase().trim()]
    );
    if (existing.rows.length > 0) {
      return res.status(409).json({ error: 'An account with this email already exists.' });
    }

    // Hash password
    const password_hash = await bcrypt.hash(password, 12);

    // Insert user
    const result = await pool.query(
      `INSERT INTO users (first_name, last_name, email, password_hash)
       VALUES ($1, $2, $3, $4)
       RETURNING id, email, first_name, last_name, is_admin`,
      [
        first_name.trim(),
        last_name.trim(),
        email.toLowerCase().trim(),
        password_hash
      ]
    );

    const user  = result.rows[0];
    const token = generateToken(user.id);
    setTokenCookie(res, token);
// Send welcome email (non-blocking)
    sendWelcomeEmail(user).catch(err =>
      console.error('Welcome email error:', err.message)
    );
    res.status(201).json({
      message: 'Account created successfully.',
      user: {
        id:         user.id,
        email:      user.email,
        first_name: user.first_name,
        last_name:  user.last_name,
        is_admin:   user.is_admin
      }
    });

  } catch (err) {
    console.error('Register error:', err.message);
    res.status(500).json({ error: 'Registration failed. Please try again.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/auth/login
// ────────────────────────────────────────────────────────
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password are required.' });
    }

    // Find user
    const result = await pool.query(
      'SELECT * FROM users WHERE email = $1',
      [email.toLowerCase().trim()]
    );

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Invalid email or password.' });
    }

    const user = result.rows[0];

    // Check password
    const valid = await bcrypt.compare(password, user.password_hash);
    if (!valid) {
      return res.status(401).json({ error: 'Invalid email or password.' });
    }

    // Check payment status
    const payment = await pool.query(
      `SELECT status FROM payments
       WHERE user_id = $1
       ORDER BY submitted_at DESC
       LIMIT 1`,
      [user.id]
    );

    const paymentStatus = payment.rows.length > 0
      ? payment.rows[0].status
      : 'none';

    // Generate token
    const token = generateToken(user.id);
    setTokenCookie(res, token);

    res.json({
      message: 'Login successful.',
      user: {
        id:             user.id,
        email:          user.email,
        first_name:     user.first_name,
        last_name:      user.last_name,
        is_admin:       user.is_admin,
        payment_status: paymentStatus
      }
    });

  } catch (err) {
    console.error('Login error:', err.message);
    res.status(500).json({ error: 'Login failed. Please try again.' });
  }
});

// ────────────────────────────────────────────────────────
// POST /api/auth/logout
// ────────────────────────────────────────────────────────
router.post('/logout', (req, res) => {
  res.clearCookie('devpath_token');
  res.json({ message: 'Logged out successfully.' });
});

// ────────────────────────────────────────────────────────
// GET /api/auth/me — get current logged in user
// ────────────────────────────────────────────────────────
router.get('/me', async (req, res) => {
  try {
    const token = req.cookies.devpath_token;
    if (!token) {
      return res.status(401).json({ error: 'Not authenticated.' });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    const result = await pool.query(
      'SELECT id, email, first_name, last_name, is_admin FROM users WHERE id = $1',
      [decoded.userId]
    );

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'User not found.' });
    }

    const user = result.rows[0];

    // Get payment status
    const payment = await pool.query(
      `SELECT status, plan, expires_at FROM payments
       WHERE user_id = $1
       ORDER BY submitted_at DESC
       LIMIT 1`,
      [user.id]
    );

    const paymentStatus = payment.rows.length > 0
      ? payment.rows[0].status
      : 'none';

    res.json({
      user: {
        id:             user.id,
        email:          user.email,
        first_name:     user.first_name,
        last_name:      user.last_name,
        is_admin:       user.is_admin,
        payment_status: paymentStatus,
        plan:           payment.rows[0]?.plan || null
      }
    });

  } catch (err) {
    res.status(401).json({ error: 'Invalid or expired session.' });
  }
});
async function sendWelcomeEmail(user) {
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
    to:      user.email,
    subject: '👋 Welcome to DevPath!',
    html: `
      <h2>Welcome to DevPath, ${user.first_name}!</h2>
      <p>Your account has been created successfully.</p>
      <p><strong>Next step:</strong> Complete your payment to unlock all courses.</p>
      <p><a href="http://localhost:3000/pay.html"
            style="background:#2563eb;color:#fff;padding:10px 24px;
                   border-radius:6px;text-decoration:none;font-weight:bold">
        Complete Payment →
      </a></p>
      <br><p>— The DevPath Team</p>
    `
  });
}
module.exports = router;
