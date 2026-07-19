const express      = require('express');
const cors         = require('cors');
const cookieParser = require('cookie-parser');
const path         = require('path');
require('dotenv').config();

const app = express();

// ── MIDDLEWARE ───────────────────────────────────────────
app.use(cors({ origin: true, credentials: true }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// ── REQUEST LOGGER ───────────────────────────────────────
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
});

// ── API ROUTES (before static files) ────────────────────
const authRoutes    = require('./routes/auth');
const paymentRoutes = require('./routes/payment');
const adminRoutes   = require('./routes/admin');

app.use('/api/auth',    authRoutes);
app.use('/api/payment', paymentRoutes);
app.use('/api/admin',   adminRoutes);

// ── HEALTH CHECK ─────────────────────────────────────────
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', time: new Date().toISOString() });
});

// ── PROTECTED ROUTES (before public static) ──────────────
// These MUST come before express.static so they are checked first
const { protect, requireVerified } = require('./middleware/protect');

// Block /paths/ — requires login + verified payment
app.use('/paths', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'paths'))(req, res, next);
});

// Block /foundations/ — requires login + verified payment
app.use('/foundations', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'foundations'))(req, res, next);
});

// Block /dashboard.html — requires login + verified payment
app.get('/dashboard.html', protect, requireVerified, (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'dashboard.html'));
});

// Block /admin.html — requires login + admin
app.get('/admin.html', protect, (req, res, next) => {
  if (!req.user.is_admin) {
    return res.redirect('/login.html?reason=admin_required');
  }
  res.sendFile(path.join(__dirname, '..', 'admin.html'));
});

// ── PUBLIC STATIC FILES (after protected routes) ─────────
// Only runs if none of the protected routes matched
app.use(express.static(path.join(__dirname, '..'), {
  index: 'index.html',
  extensions: ['html']
}));

// ── 404 HANDLER ──────────────────────────────────────────
app.use((req, res) => {
  if (req.path.startsWith('/api/')) {
    return res.status(404).json({ error: 'Route not found' });
  }
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

// ── GLOBAL ERROR HANDLER ─────────────────────────────────
app.use((err, req, res, next) => {
  console.error('❌ Server error:', err.message);
  if (req.path.startsWith('/api/')) {
    return res.status(500).json({ error: 'Internal server error' });
  }
  res.status(500).send('Something went wrong. Please try again.');
});

// ── HANDLE UNCAUGHT ERRORS ───────────────────────────────
process.on('uncaughtException', err => {
  console.error('❌ Uncaught Exception:', err.message);
});

process.on('unhandledRejection', reason => {
  console.error('❌ Unhandled Rejection:', reason);
});

// ── START SERVER ─────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ DevPath server running on http://localhost:${PORT}`);
});
