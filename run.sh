#!/bin/bash
redis-server /etc/redis/redis.conf &
service sendmail start &
python3 DomainNameSystemServer.py &
python3 HTTPServer.py &
celery -A Web worker -B --loglevel=info --pool=solo &
nginx &
gunicorn Web.wsgi:application --bind 0.0.0.0:9999 --workers 6


