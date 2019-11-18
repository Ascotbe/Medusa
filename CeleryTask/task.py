from __future__ import absolute_import, unicode_literals
from MedusaWeb.celery import app  # 从我的Celery中导入App
import time

@app.task(name='tasks.add')     # 需要配置 name='tasks.add'，否则报 Received unregistered task of type 'app.tasks.add'.
def add(x, y):
    time.sleep(10)
    return x + y


@app.task(name='tasks.mul')
def mul(x, y):
    time.sleep(10)
    return x * y