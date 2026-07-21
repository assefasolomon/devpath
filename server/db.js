const { Pool } = require('pg');
require('dotenv').config();

let poolConfig;

// Render provides DATABASE_URL — use it if available
if (process.env.DATABASE_URL) {
  poolConfig = {
    connectionString: process.env.DATABASE_URL,
    ssl: process.env.NODE_ENV === 'production'
      ? { rejectUnauthorized: false }
      : false
  };
} else {
  // Local development
  poolConfig = {
    host:     process.env.DB_HOST     || 'localhost',
    port:     parseInt(process.env.DB_PORT) || 5432,
    database: process.env.DB_NAME     || 'devpath',
    user:     process.env.DB_USER     || 'devpath_user',
    password: process.env.DB_PASSWORD || 'devpath123',
  };
}

const pool = new Pool(poolConfig);

pool.connect((err, client, release) => {
  if (err) {
    console.error('❌ Database connection failed:', err.message);
  } else {
    console.log('✅ Database connected');
    release();
  }
});

module.exports = pool;
