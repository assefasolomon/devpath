module.exports = {
  apps: [{
    name:        'devpath',
    script:      'server.js',
    cwd:         '/home/solomon/devpath/server',
    instances:   1,
    autorestart: true,
    watch:       false,
    max_memory_restart: '200M',
    env: {
      NODE_ENV: 'development',
      PORT:     3000
    },
    error_file:  '/home/solomon/devpath/server/logs/error.log',
    out_file:    '/home/solomon/devpath/server/logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss'
  }]
};
