const express      = require('express');
const cors         = require('cors');
const cookieParser = require('cookie-parser');
const path         = require('path');
require('dotenv').config();

const app = express();

app.use(cors({ origin: true, credentials: true }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
});

// ── API ROUTES ────────────────────────────────────────────
const authRoutes    = require('./routes/auth');
const paymentRoutes = require('./routes/payment');
const adminRoutes   = require('./routes/admin');

app.use('/api/auth',    authRoutes);
app.use('/api/payment', paymentRoutes);
app.use('/api/admin',   adminRoutes);

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', time: new Date().toISOString() });
});

// ── PROTECTED ROUTES — must come before static ────────────
const { protect, requireVerified } = require('./middleware/protect');

app.use('/paths', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'paths'))(req, res, next);
});

app.use('/foundations', protect, requireVerified, (req, res, next) => {
  express.static(path.join(__dirname, '..', 'foundations'))(req, res, next);
});

app.get('/dashboard.html', protect, (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'dashboard.html'));
});

app.get('/admin.html', protect, (req, res) => {
  if (!req.user.is_admin) {
    return res.redirect('/login.html?reason=admin_required');
  }
  res.sendFile(path.join(__dirname, '..', 'admin.html'));
});

// ── PUBLIC STATIC — after protected routes ────────────────
app.use(express.static(path.join(__dirname, '..'), {
  index: 'index.html',
  extensions: ['html']
}));

// ── 404 ───────────────────────────────────────────────────
app.use((req, res) => {
  if (req.path.startsWith('/api/')) {
    return res.status(404).json({ error: 'Route not found' });
  }
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

// ── ERROR HANDLER ─────────────────────────────────────────
app.use((err, req, res, next) => {
  console.error('Server error:', err.message);
  if (req.path.startsWith('/api/')) {
    return res.status(500).json({ error: 'Internal server error' });
  }
  res.status(500).send('Something went wrong.');
});

process.on('uncaughtException',   err => console.error('Uncaught:', err.message));
process.on('unhandledRejection',  err => console.error('Unhandled:', err));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ DevPath server: http://localhost:${PORT}`);
});
