const jwt  = require('jsonwebtoken');
const pool = require('../db');
require('dotenv').config();

async function protect(req, res, next) {
  try {
    const token = req.cookies?.devpath_token;

    if (!token) {
      if (req.path.startsWith('/api/')) {
        return res.status(401).json({ error: 'Not authenticated.' });
      }
      return res.redirect('/login.html?reason=login_required');
    }

    let decoded;
    try {
      decoded = jwt.verify(token, process.env.JWT_SECRET);
    } catch (jwtErr) {
      res.clearCookie('devpath_token');
      if (req.path.startsWith('/api/')) {
        return res.status(401).json({ error: 'Session expired.' });
      }
      return res.redirect('/login.html?reason=session_expired');
    }

    const result = await pool.query(
      'SELECT id, email, first_name, last_name, is_admin FROM users WHERE id = $1',
      [decoded.userId]
    );

    if (result.rows.length === 0) {
      res.clearCookie('devpath_token');
      if (req.path.startsWith('/api/')) {
        return res.status(401).json({ error: 'User not found.' });
      }
      return res.redirect('/login.html?reason=account_not_found');
    }

    req.user = result.rows[0];
    next();

  } catch (err) {
    console.error('protect error:', err.message);
    res.clearCookie('devpath_token');
    if (req.path.startsWith('/api/')) {
      return res.status(500).json({ error: 'Authentication error.' });
    }
    return res.redirect('/login.html?reason=error');
  }
}

async function requireVerified(req, res, next) {
  try {
    if (req.user?.is_admin) return next();

    const result = await pool.query(
      `SELECT status FROM payments
       WHERE user_id = $1 AND status = 'verified'
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (result.rows.length > 0) {
      return next();
    }

    // Check for pending
    const pending = await pool.query(
      `SELECT status, user_tx_id FROM payments
       WHERE user_id = $1
       ORDER BY submitted_at DESC LIMIT 1`,
      [req.user.id]
    );

    if (pending.rows.length > 0) {
      const p = pending.rows[0];
      if (p.status === 'pending' && p.user_tx_id) {
        // Submitted and waiting
        return res.redirect('/dashboard.html?status=pending');
      }
      if (p.status === 'pending' && !p.user_tx_id) {
        // Has reference but not submitted yet
        return res.redirect('/submit-payment.html');
      }
      if (p.status === 'rejected') {
        return res.redirect('/pay.html?reason=rejected');
      }
    }

    return res.redirect('/pay.html?reason=payment_required');

  } catch (err) {
    console.error('requireVerified error:', err.message);
    return res.redirect('/pay.html?reason=error');
  }
}

async function requireAdmin(req, res, next) {
  try {
    if (!req.user?.is_admin) {
      if (req.path.startsWith('/api/')) {
        return res.status(403).json({ error: 'Admin access required.' });
      }
      return res.redirect('/login.html?reason=admin_required');
    }
    next();
  } catch (err) {
    console.error('requireAdmin error:', err.message);
    res.status(500).json({ error: 'Authorization error.' });
  }
}

module.exports = { protect, requireVerified, requireAdmin };
