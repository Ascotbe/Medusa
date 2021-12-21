# celery -A Web worker -B --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# 测试启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# pip install python-magic-bin==0.4.14
# from jinja2 import Template
# a="aa{{'{'}}{{sds}}{{'}'}}"
# Tmp = Template(a)
# c=Tmp.render(sds="dddddd")  # 处理占位符
# print(c)
import ClassCongregation
a=ClassCongregation.Binary().String2GoArray("\xff\xfa\xfb\xfc\xfd\xfe\xff")
print(a)

