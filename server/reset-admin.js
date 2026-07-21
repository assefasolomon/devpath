/**
 * DevPath Admin Password Reset Tool
 * Usage: node reset-admin.js [email] [password]
 * Example: node reset-admin.js devpath451@gmail.com MyNewPassword123
 */

const bcrypt = require('bcryptjs');
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host:     process.env.DB_HOST,
  port:     process.env.DB_PORT,
  database: process.env.DB_NAME,
  user:     process.env.DB_USER,
  password: process.env.DB_PASSWORD
});

async function resetAdmin() {
  const adminEmail    = process.argv[2] || process.env.ADMIN_EMAIL || 'devpath451@gmail.com';
  const adminPassword = process.argv[3] || 'DevPath@2025';

  if (adminPassword.length < 8) {
    console.error('❌ Password must be at least 8 characters.');
    process.exit(1);
  }

  console.log(`\n🔧 DevPath Admin Reset Tool`);
  console.log(`   Email:    ${adminEmail}`);
  console.log(`   Password: ${'*'.repeat(adminPassword.length)}\n`);

  try {
    const hash   = await bcrypt.hash(adminPassword, 12);
    const result = await pool.query(
      `INSERT INTO users (email, password_hash, first_name, last_name, is_admin)
       VALUES ($1, $2, 'Admin', 'DevPath', TRUE)
       ON CONFLICT (email)
       DO UPDATE SET password_hash = $2, is_admin = TRUE
       RETURNING id, email, is_admin`,
      [adminEmail, hash]
    );

    const admin = result.rows[0];
    console.log(`✅ Admin account ready:`);
    console.log(`   ID:       ${admin.id}`);
    console.log(`   Email:    ${admin.email}`);
    console.log(`   Is Admin: ${admin.is_admin}`);
    console.log(`\n📋 Login credentials:`);
    console.log(`   URL:      http://localhost:3000/admin.html`);
    console.log(`   Email:    ${adminEmail}`);
    console.log(`   Password: ${adminPassword}\n`);

    process.exit(0);
  } catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
  }
}

resetAdmin();
