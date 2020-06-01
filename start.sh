#!/bin/bash
nohup python3 manage.py runserver 0.0.0.0:9999 &
redis-server /etc/redis/redis.conf
nohup celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo &
