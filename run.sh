#!/bin/bash
cd /Medusa/Vue
nohup npm run serve &
cd /Medusa
nohup redis-server /etc/redis/redis.conf & 
nohup celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo & 
python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
