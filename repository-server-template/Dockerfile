FROM ubuntu:latest
RUN apt update && apt upgrade -y && apt install nginx cron git -y && service cron start && service nginx start \
    && cd /var/www/html && git clone https://github.com/bluemiaomiao/jjvmm-repo.git \
    && echo '*/5 * * * * www-data cd /var/www/html && git clone https://github.com/bluemiaomiao/jjvmm-repo.git' >> /etc/crontab
