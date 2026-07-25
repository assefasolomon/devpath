/**
 * Freelance Skills Hub — Production Setup Script
 * Creates all database tables + admin account
 * Safe to run multiple times (uses IF NOT EXISTS)
 * Usage: node setup-production.js
 */

const { Pool } = require('pg');
const bcrypt   = require('bcryptjs');
require('dotenv').config();

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function setup() {
  const client = await pool.connect();

  try {
    console.log('\n🔧 Freelance Skills Hub — Production Setup\n');

    // Users table
    await client.query(`
      CREATE TABLE IF NOT EXISTS users (
        id            SERIAL PRIMARY KEY,
        email         VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        first_name    VARCHAR(100) NOT NULL,
        last_name     VARCHAR(100) NOT NULL,
        is_admin      BOOLEAN DEFAULT FALSE,
        created_at    TIMESTAMP DEFAULT NOW()
      )
    `);
    console.log('✅ users table ready');

    // Payments table
    await client.query(`
      CREATE TABLE IF NOT EXISTS payments (
        id             SERIAL PRIMARY KEY,
        user_id        INTEGER REFERENCES users(id) ON DELETE CASCADE,
        plan           VARCHAR(50) NOT NULL,
        amount         DECIMAL(10,2) NOT NULL,
        currency       VARCHAR(10) DEFAULT 'ETB',
        reference_code VARCHAR(20) UNIQUE NOT NULL,
        user_tx_id     VARCHAR(255),
        payment_method VARCHAR(50),
        status         VARCHAR(20) DEFAULT 'pending',
        submitted_at   TIMESTAMP DEFAULT NOW(),
        verified_at    TIMESTAMP,
        verified_by    INTEGER REFERENCES users(id),
        expires_at     TIMESTAMP,
        notes          TEXT
      )
    `);
    console.log('✅ payments table ready');

    // Sessions table
    await client.query(`
      CREATE TABLE IF NOT EXISTS sessions (
        id         SERIAL PRIMARY KEY,
        user_id    INTEGER REFERENCES users(id) ON DELETE CASCADE,
        token_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW(),
        expires_at TIMESTAMP DEFAULT NOW() + INTERVAL '30 days'
      )
    `);
    console.log('✅ sessions table ready');

    // Indexes
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_user_id        ON payments(user_id)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_status          ON payments(status)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_reference_code  ON payments(reference_code)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_sessions_user_id         ON sessions(user_id)`);
    console.log('✅ indexes ready');

    // Create or reset admin account
    const adminEmail    = process.env.ADMIN_EMAIL    || 'devpath451@gmail.com';
    const adminPassword = process.env.ADMIN_PASSWORD || 'DevPath@2025';
    const hash          = await bcrypt.hash(adminPassword, 12);

    const result = await client.query(
      `INSERT INTO users (email, password_hash, first_name, last_name, is_admin)
       VALUES ($1, $2, 'Admin', 'FSH', TRUE)
       ON CONFLICT (email)
       DO UPDATE SET password_hash = $2, is_admin = TRUE
       RETURNING id, email, is_admin`,
      [adminEmail, hash]
    );

    const adminId = result.rows[0].id;
    console.log(`✅ Admin account ready — email: ${result.rows[0].email}`);

    // Remove any payment records for admin (admin should never have payments)
    await client.query(
      `DELETE FROM payments WHERE user_id = $1`,
      [adminId]
    );
    console.log('✅ Admin payment records cleaned');

    console.log('\n🎉 Setup complete!');
    console.log(`   Admin email:    ${adminEmail}`);
    console.log(`   Admin password: ${adminPassword}`);
    console.log(`   Admin panel:    https://freelance-skills-hub.onrender.com/admin.html\n`);

  } catch (err) {
    console.error('❌ Setup error:', err.message);
    throw err;
  } finally {
    client.release();
    await pool.end();
  }
}

setup().catch(err => {
  console.error(err);
  process.exit(1);
});
