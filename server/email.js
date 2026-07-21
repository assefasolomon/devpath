const nodemailer = require('nodemailer');
require('dotenv').config();

const BRAND    = 'Freelance Skills Hub';
const APP_URL  = process.env.APP_URL || 'http://localhost:3000';
const BRAND_COLOR = '#14532D';

function createTransporter() {
  if (!process.env.SMTP_USER || !process.env.SMTP_PASS ||
      process.env.SMTP_PASS === 'your_16_char_app_password_here') return null;
  return nodemailer.createTransport({
    host:   process.env.SMTP_HOST   || 'smtp.gmail.com',
    port:   parseInt(process.env.SMTP_PORT) || 587,
    secure: false,
    auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS }
  });
}

function baseTemplate(content) {
  return `
  <div style="font-family:'Inter',Arial,sans-serif;max-width:600px;margin:0 auto;background:#fff">
    <div style="background:${BRAND_COLOR};padding:24px 32px;border-radius:12px 12px 0 0">
      <div style="display:flex;align-items:center;gap:10px">
        <div style="width:36px;height:36px;background:rgba(255,255,255,.15);border-radius:8px;display:inline-flex;align-items:center;justify-content:center">
          <span style="color:#fff;font-size:16px;font-weight:700">F</span>
        </div>
        <span style="color:#fff;font-size:18px;font-weight:700">${BRAND}</span>
      </div>
    </div>
    <div style="padding:32px;background:#fff">
      ${content}
    </div>
    <div style="background:#F8FAFC;padding:20px 32px;border-top:1px solid #E2E8F0;border-radius:0 0 12px 12px;text-align:center">
      <p style="font-size:12px;color:#94A3B8;margin:0">
        © 2025 ${BRAND} · Built for Ethiopian developers<br>
        Pay via Telebirr or CBE · Learn anywhere, anytime
      </p>
    </div>
  </div>`;
}

function btn(text, url) {
  return `<a href="${url}" style="display:inline-block;background:${BRAND_COLOR};color:#fff;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:700;font-size:15px;margin:20px 0">${text}</a>`;
}

function table(rows) {
  const cells = rows.map(([label, value, color]) =>
    `<tr>
      <td style="padding:10px 16px;border-bottom:1px solid #E2E8F0;color:#64748B;font-size:14px;width:40%">${label}</td>
      <td style="padding:10px 16px;border-bottom:1px solid #E2E8F0;font-weight:600;font-size:14px;color:${color || '#0F172A'}">${value}</td>
    </tr>`
  ).join('');
  return `<table style="width:100%;border-collapse:collapse;background:#F8FAFC;border-radius:8px;overflow:hidden;margin:16px 0">${cells}</table>`;
}

async function sendEmail(to, subject, html) {
  const transporter = createTransporter();
  if (!transporter) {
    console.log(`[EMAIL SKIP] No SMTP. Would send to ${to}: ${subject}`);
    return;
  }
  try {
    await transporter.sendMail({
      from: `"${BRAND}" <${process.env.SMTP_USER}>`,
      to, subject, html
    });
    console.log(`[EMAIL SENT] ${to} | ${subject}`);
  } catch (err) {
    console.error(`[EMAIL ERROR] ${err.message}`);
  }
}

async function sendWelcomeEmail(user) {
  await sendEmail(
    user.email,
    `👋 Welcome to ${BRAND}!`,
    baseTemplate(`
      <h2 style="color:#0F172A;font-size:22px;margin:0 0 8px">Welcome, ${user.first_name}! 🎉</h2>
      <p style="color:#64748B;font-size:15px;line-height:1.7;margin:0 0 20px">
        Your account has been created successfully. You are one step away from accessing
        all 4 learning paths and 200+ lessons on ${BRAND}.
      </p>
      <p style="color:#0F172A;font-weight:700;font-size:15px;margin:0 0 8px">Next step: Complete your payment</p>
      <p style="color:#64748B;font-size:14px;line-height:1.7;margin:0 0 20px">
        Transfer 599 ETB via Telebirr or CBE to unlock all courses immediately.
      </p>
      ${btn('Complete Payment →', APP_URL + '/pay.html')}
      <p style="color:#94A3B8;font-size:13px;margin:20px 0 0">
        Questions? Reply to this email and we will help you.
      </p>
    `)
  );
}

async function sendPaymentSubmittedEmail(user, payment) {
  await sendEmail(
    user.email,
    `✅ Payment Received — ${BRAND}`,
    baseTemplate(`
      <h2 style="color:#0F172A;font-size:22px;margin:0 0 8px">Payment Received, ${user.first_name}!</h2>
      <p style="color:#64748B;font-size:15px;line-height:1.7;margin:0 0 20px">
        We have received your payment submission and are verifying your transfer.
        This usually takes <strong>1–2 hours</strong> during business hours (8am–8pm).
      </p>
      ${table([
        ['Reference Code', payment.reference_code, '#14532D'],
        ['Transaction ID', payment.user_tx_id, '#0F172A'],
        ['Amount', payment.amount + ' ETB', '#0F172A'],
        ['Status', '⏳ Pending Verification', '#D97706'],
      ])}
      ${btn('Check Payment Status →', APP_URL + '/dashboard.html')}
      <p style="color:#94A3B8;font-size:13px;margin:20px 0 0">
        You will receive another email once your payment is verified.
      </p>
    `)
  );
}

async function sendPaymentVerifiedEmail(user, payment) {
  await sendEmail(
    user.email,
    `🎉 Payment Verified — You Have Full Access!`,
    baseTemplate(`
      <h2 style="color:#166534;font-size:22px;margin:0 0 8px">You're in, ${user.first_name}! 🚀</h2>
      <p style="color:#64748B;font-size:15px;line-height:1.7;margin:0 0 20px">
        Your payment has been <strong style="color:#166534">verified</strong>.
        Your ${BRAND} Full Access is now <strong>active</strong>.
        You can start learning immediately.
      </p>
      ${table([
        ['Plan', BRAND + ' Full Access', '#0F172A'],
        ['Amount Paid', payment.amount + ' ETB', '#0F172A'],
        ['Status', '✅ Verified — Lifetime Access', '#166534'],
      ])}
      <p style="color:#0F172A;font-weight:700;font-size:15px;margin:0 0 8px">Your courses:</p>
      <ul style="color:#64748B;font-size:14px;line-height:2;margin:0 0 20px;padding-left:20px">
        <li>🧱 Web Development Foundations</li>
        <li>⚡ Full Stack JavaScript (React, Node.js)</li>
        <li>💎 Full Stack Ruby on Rails</li>
        <li>🐍 Python for AI (NumPy, Pandas, Matplotlib)</li>
      </ul>
      ${btn('Start Learning Now →', APP_URL + '/dashboard.html')}
    `)
  );
}

async function sendPaymentRejectedEmail(user, payment, notes) {
  await sendEmail(
    user.email,
    `⚠ Payment Could Not Be Verified — ${BRAND}`,
    baseTemplate(`
      <h2 style="color:#991B1B;font-size:22px;margin:0 0 8px">Payment Not Verified</h2>
      <p style="color:#64748B;font-size:15px;line-height:1.7;margin:0 0 20px">
        Hi ${user.first_name}, unfortunately we could not verify your payment.
      </p>
      ${table([
        ['Reference Code', payment.reference_code, '#0F172A'],
        ['Reason', notes || 'Payment could not be verified', '#DC2626'],
      ])}
      <p style="color:#0F172A;font-weight:700;font-size:15px;margin:20px 0 8px">What to do next:</p>
      <ol style="color:#64748B;font-size:14px;line-height:2;margin:0 0 20px;padding-left:20px">
        <li>Check that you transferred the correct amount (599 ETB)</li>
        <li>Make sure you included your reference code in the note/description</li>
        <li>Submit your payment again with the correct transaction ID</li>
      </ol>
      ${btn('Try Again →', APP_URL + '/pay.html')}
      <p style="color:#94A3B8;font-size:13px;margin:20px 0 0">
        If you believe this is an error, reply to this email with your transaction receipt.
      </p>
    `)
  );
}

module.exports = {
  sendWelcomeEmail,
  sendPaymentSubmittedEmail,
  sendPaymentVerifiedEmail,
  sendPaymentRejectedEmail
};
