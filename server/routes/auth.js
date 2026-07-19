const express  = require('express');
const bcrypt   = require('bcryptjs');
const jwt      = require('jsonwebtoken');
const pool     = require('../db');
const email    = require('../email');
require('dotenv').config();

const router = express.Router();

function generateToken(userId) {
  return jwt.sign({ userId }, process.env.JWT_SECRET, { expiresIn: '30d' });
}

function setTokenCookie(res, token) {
  res.cookie('devpath_token', token, {
    httpOnly: true,
    secure:   process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge:   30 * 24 * 60 * 60 * 1000
  });
}

async function getPaymentStatus(userId) {
  const result = await pool.query(
    `SELECT status FROM payments WHERE user_id = $1
     ORDER BY submitted_at DESC LIMIT 1`,
    [userId]
  );
  return result.rows.length > 0 ? result.rows[0].status : 'none';
}

// POST /api/auth/register
router.post('/register', async (req, res) => {
  try {
    const { first_name, last_name, email: userEmail, password } = req.body;

    if (!first_name?.trim() || !last_name?.trim() || !userEmail?.trim() || !password) {
      return res.status(400).json({ error: 'All fields are required.' });
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userEmail)) {
      return res.status(400).json({ error: 'Please enter a valid email address.' });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: 'Password must be at least 6 characters.' });
    }

    const existing = await pool.query(
      'SELECT id FROM users WHERE email = $1',
      [userEmail.toLowerCase().trim()]
    );
    if (existing.rows.length > 0) {
      return res.status(409).json({ error: 'An account with this email already exists.' });
    }

    const password_hash = await bcrypt.hash(password, 12);

    const result = await pool.query(
      `INSERT INTO users (first_name, last_name, email, password_hash)
       VALUES ($1, $2, $3, $4)
       RETURNING id, email, first_name, last_name, is_admin`,
      [
        first_name.trim(),
        last_name.trim(),
        userEmail.toLowerCase().trim(),
        password_hash
      ]
    );

    const user  = result.rows[0];
    const token = generateToken(user.id);
    setTokenCookie(res, token);

    // Send welcome email (non-blocking)
    email.sendWelcomeEmail(user).catch(() => {});

    res.status(201).json({
      message: 'Account created successfully.',
      user: {
        id:             user.id,
        email:          user.email,
        first_name:     user.first_name,
        last_name:      user.last_name,
        is_admin:       user.is_admin,
        payment_status: 'none'
      }
    });

  } catch (err) {
    console.error('Register error:', err.message);
    res.status(500).json({ error: 'Registration failed. Please try again.' });
  }
});

// POST /api/auth/login
router.post('/login', async (req, res) => {
  try {
    const { email: userEmail, password } = req.body;

    if (!userEmail?.trim() || !password) {
      return res.status(400).json({ error: 'Email and password are required.' });
    }

    const result = await pool.query(
      'SELECT * FROM users WHERE email = $1',
      [userEmail.toLowerCase().trim()]
    );

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Invalid email or password.' });
    }

    const user = result.rows[0];
    const valid = await bcrypt.compare(password, user.password_hash);

    if (!valid) {
      return res.status(401).json({ error: 'Invalid email or password.' });
    }

    const paymentStatus = await getPaymentStatus(user.id);
    const token         = generateToken(user.id);
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

// POST /api/auth/logout
router.post('/logout', (req, res) => {
  res.clearCookie('devpath_token');
  res.json({ message: 'Logged out successfully.' });
});

// GET /api/auth/me
router.get('/me', async (req, res) => {
  try {
    const token = req.cookies?.devpath_token;
    if (!token) return res.status(401).json({ error: 'Not authenticated.' });

    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    const result = await pool.query(
      'SELECT id, email, first_name, last_name, is_admin FROM users WHERE id = $1',
      [decoded.userId]
    );

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'User not found.' });
    }

    const user          = result.rows[0];
    const paymentStatus = await getPaymentStatus(user.id);

    const paymentRow = await pool.query(
      `SELECT plan, reference_code FROM payments WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [user.id]
    );

    res.json({
      user: {
        id:             user.id,
        email:          user.email,
        first_name:     user.first_name,
        last_name:      user.last_name,
        is_admin:       user.is_admin,
        payment_status: paymentStatus,
        plan:           paymentRow.rows[0]?.plan || null
      }
    });

  } catch (err) {
    console.error('Me error:', err.message);
    res.status(401).json({ error: 'Invalid or expired session.' });
  }
});

module.exports = router;
