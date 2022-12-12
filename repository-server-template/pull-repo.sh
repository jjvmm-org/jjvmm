#!/usr/bin/env bash
service nginx start && service cron start
cd /var/www/html && git clone https://github.com/jjvmm-org/index.git
echo '*/5 * * * * www-data cd /var/www/html && git clone https://github.com/jjvmm-org/index.git' >> /etc/crontab
tail -f /dev/null