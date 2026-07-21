/**
 * Database initialization script
 * Run this after deploying to Render to create all tables
 * Usage: node init-db.js
 */

const { Pool } = require('pg');
const bcrypt   = require('bcryptjs');
require('dotenv').config();

let poolConfig;
if (process.env.DATABASE_URL) {
  poolConfig = {
    connectionString: process.env.DATABASE_URL,
    ssl: { rejectUnauthorized: false }
  };
} else {
  poolConfig = {
    host:     process.env.DB_HOST,
    port:     parseInt(process.env.DB_PORT) || 5432,
    database: process.env.DB_NAME,
    user:     process.env.DB_USER,
    password: process.env.DB_PASSWORD,
  };
}

const pool = new Pool(poolConfig);

async function initDb() {
  const client = await pool.connect();

  try {
    console.log('🔧 Initializing Freelance Skills Hub database...\n');

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
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_user_id      ON payments(user_id)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_status        ON payments(status)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_payments_reference_code ON payments(reference_code)`);
    await client.query(`CREATE INDEX IF NOT EXISTS idx_sessions_user_id       ON sessions(user_id)`);
    console.log('✅ indexes ready');

    // Create admin user
    const adminEmail    = process.env.ADMIN_EMAIL    || 'devpath451@gmail.com';
    const adminPassword = process.env.ADMIN_PASSWORD || 'DevPath@2025';

    const hash = await bcrypt.hash(adminPassword, 12);
    const result = await client.query(
      `INSERT INTO users (email, password_hash, first_name, last_name, is_admin)
       VALUES ($1, $2, 'Admin', 'FSH', TRUE)
       ON CONFLICT (email) DO UPDATE
         SET password_hash = $2, is_admin = TRUE
       RETURNING id, email, is_admin`,
      [adminEmail, hash]
    );

    console.log(`\n✅ Admin account ready:`);
    console.log(`   Email:    ${result.rows[0].email}`);
    console.log(`   Password: ${adminPassword}`);
    console.log(`\n🎉 Database initialization complete!\n`);

  } catch (err) {
    console.error('❌ Database init error:', err.message);
    throw err;
  } finally {
    client.release();
    await pool.end();
  }
}

initDb().catch(err => {
  console.error(err);
  process.exit(1);
});
