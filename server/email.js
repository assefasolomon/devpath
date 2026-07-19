const nodemailer = require('nodemailer');
require('dotenv').config();

function createTransporter() {
  if (!process.env.SMTP_USER || !process.env.SMTP_PASS) return null;
  return nodemailer.createTransport({
    host:   process.env.SMTP_HOST   || 'smtp.gmail.com',
    port:   parseInt(process.env.SMTP_PORT) || 587,
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });
}

async function sendEmail(to, subject, html) {
  const transporter = createTransporter();
  if (!transporter) {
    console.log(`[EMAIL SKIP] No SMTP config. Would send to ${to}: ${subject}`);
    return;
  }
  try {
    await transporter.sendMail({
      from: `"DevPath" <${process.env.SMTP_USER}>`,
      to, subject, html
    });
    console.log(`[EMAIL SENT] To: ${to} | ${subject}`);
  } catch (err) {
    console.error(`[EMAIL ERROR] ${err.message}`);
  }
}

const APP_URL = process.env.APP_URL || 'http://localhost:3000';

async function sendWelcomeEmail(user) {
  await sendEmail(
    user.email,
    '👋 Welcome to DevPath!',
    `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px">
      <h2 style="color:#2563eb">Welcome to DevPath, ${user.first_name}!</h2>
      <p>Your account has been created successfully.</p>
      <p>To access your courses, complete your payment:</p>
      <a href="${APP_URL}/pay.html"
         style="display:inline-block;background:#2563eb;color:#fff;padding:12px 28px;
                border-radius:6px;text-decoration:none;font-weight:bold;margin:16px 0">
        Complete Payment →
      </a>
      <p style="color:#666;font-size:14px">— The DevPath Team</p>
    </div>
    `
  );
}

async function sendPaymentSubmittedEmail(user, payment) {
  await sendEmail(
    user.email,
    '✅ Payment Received — DevPath',
    `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px">
      <h2 style="color:#2563eb">Hi ${user.first_name},</h2>
      <p>We received your payment submission and are verifying it.</p>
      <table style="width:100%;border-collapse:collapse;margin:16px 0">
        <tr style="background:#f3f4f6">
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Reference Code</td>
          <td style="padding:10px;border:1px solid #e5e7eb;font-family:monospace;font-size:16px;color:#2563eb">${payment.reference_code}</td>
        </tr>
        <tr>
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Transaction ID</td>
          <td style="padding:10px;border:1px solid #e5e7eb">${payment.user_tx_id}</td>
        </tr>
        <tr style="background:#f3f4f6">
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Amount</td>
          <td style="padding:10px;border:1px solid #e5e7eb">${payment.amount} ETB</td>
        </tr>
        <tr>
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Status</td>
          <td style="padding:10px;border:1px solid #e5e7eb;color:#d97706;font-weight:bold">⏳ Pending Verification</td>
        </tr>
      </table>
      <p>We verify payments within <strong>1–2 hours</strong> during business hours (8am–8pm).</p>
      <p>You can check your status at any time:</p>
      <a href="${APP_URL}/dashboard.html"
         style="display:inline-block;background:#2563eb;color:#fff;padding:12px 28px;
                border-radius:6px;text-decoration:none;font-weight:bold;margin:16px 0">
        View Payment Status →
      </a>
      <p style="color:#666;font-size:14px">— The DevPath Team</p>
    </div>
    `
  );
}

async function sendPaymentVerifiedEmail(user, payment) {
  await sendEmail(
    user.email,
    '🎉 Payment Verified — You Have Full Access!',
    `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px">
      <h2 style="color:#10b981">Payment Verified, ${user.first_name}!</h2>
      <p>Your payment has been approved. Your DevPath Full Access is now <strong>active</strong>.</p>
      <table style="width:100%;border-collapse:collapse;margin:16px 0">
        <tr style="background:#f3f4f6">
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Plan</td>
          <td style="padding:10px;border:1px solid #e5e7eb">DevPath Full Access</td>
        </tr>
        <tr>
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Amount Paid</td>
          <td style="padding:10px;border:1px solid #e5e7eb">${payment.amount} ETB</td>
        </tr>
        <tr style="background:#f3f4f6">
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Access</td>
          <td style="padding:10px;border:1px solid #e5e7eb;color:#10b981;font-weight:bold">✅ Lifetime Access</td>
        </tr>
      </table>
      <p>You now have access to all 4 learning paths and 200+ lessons.</p>
      <a href="${APP_URL}/dashboard.html"
         style="display:inline-block;background:#10b981;color:#fff;padding:12px 28px;
                border-radius:6px;text-decoration:none;font-weight:bold;margin:16px 0">
        Start Learning Now →
      </a>
      <p style="color:#666;font-size:14px">— The DevPath Team</p>
    </div>
    `
  );
}

async function sendPaymentRejectedEmail(user, payment, notes) {
  await sendEmail(
    user.email,
    '⚠️ Payment Could Not Be Verified — DevPath',
    `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px">
      <h2 style="color:#ef4444">Payment Not Verified</h2>
      <p>Hi ${user.first_name}, unfortunately we could not verify your payment.</p>
      <table style="width:100%;border-collapse:collapse;margin:16px 0">
        <tr style="background:#f3f4f6">
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Reference Code</td>
          <td style="padding:10px;border:1px solid #e5e7eb;font-family:monospace">${payment.reference_code}</td>
        </tr>
        <tr>
          <td style="padding:10px;border:1px solid #e5e7eb;font-weight:bold">Reason</td>
          <td style="padding:10px;border:1px solid #e5e7eb;color:#ef4444">${notes || 'Payment could not be verified'}</td>
        </tr>
      </table>
      <p>Please check your transaction details and try again, or contact us for help.</p>
      <a href="${APP_URL}/submit-payment.html"
         style="display:inline-block;background:#2563eb;color:#fff;padding:12px 28px;
                border-radius:6px;text-decoration:none;font-weight:bold;margin:16px 0">
        Try Again →
      </a>
      <p style="color:#666;font-size:14px">— The DevPath Team</p>
    </div>
    `
  );
}

module.exports = {
  sendWelcomeEmail,
  sendPaymentSubmittedEmail,
  sendPaymentVerifiedEmail,
  sendPaymentRejectedEmail
};
