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

// ── PUBLIC STATIC FILES ──────────────────────────────────
// Serve everything in devpath/ EXCEPT /paths/ (which is protected below)
app.use(express.static(path.join(__dirname, '..'), {
  index: 'index.html',
  extensions: ['html']
}));

// ── API ROUTES ───────────────────────────────────────────
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

// ── PROTECTED ROUTES ─────────────────────────────────────
const { protect, requireVerified } = require('./middleware/protect');

// Protect /paths/ directory — must be logged in AND verified
app.use('/paths', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'paths'))(req, res, next);
});

// Protect /foundations/ directory
app.use('/foundations', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'foundations'))(req, res, next);
});

// Protect dashboard
app.get('/dashboard.html', protect, requireVerified, (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'dashboard.html'));
});

// ── CATCH-ALL: serve index.html for unknown routes ───────
app.use((req, res, next) => {
  // If it's an API route that wasn't matched
  if (req.path.startsWith('/api/')) {
    return res.status(404).json({ error: 'Route not found' });
  }
  // For everything else serve index.html
  const file = path.join(__dirname, '..', 'index.html');
  res.sendFile(file, err => {
    if (err) res.status(404).send('Page not found');
  });
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

process.on('unhandledRejection', (reason) => {
  console.error('❌ Unhandled Rejection:', reason);
});

// ── START SERVER ─────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ DevPath server running on http://localhost:${PORT}`);
  console.log(`   Home:    http://localhost:${PORT}`);
  console.log(`   Admin:   http://localhost:${PORT}/admin.html`);
  console.log(`   Login:   http://localhost:${PORT}/login.html`);
});
