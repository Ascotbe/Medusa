from celery import Celery

from celery.schedules import crontab
import time


# 消息中间件，密码是你redis的密码
# broker='redis://:123456@127.0.0.1:6379/2' 密码123456
broker = 'redis://127.0.0.1:12345/0'  # 无密码
# 任务结果存储
backend = 'redis://127.0.0.1:12345/1'
#https://www.cnblogs.com/midworld/p/10960465.html
# 生成celery对象，'task'相当于key，用于区分celery对象
# include参数需要指定任务模块
app = Celery('task', broker=broker, backend=backend,include=['CeleryTask.task'])#这边的值是要导入的文件夹中的文件

# 时区
app.conf.timezone = 'Asia/Shanghai'

