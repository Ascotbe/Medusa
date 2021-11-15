# celery -A Web worker --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# 测试启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# pip install python-magic-bin==0.4.14

# b=""
# import requests
# a=requests.get('https://www.v2ex.com/favicon.ico')
# if a.raw.version== 10:
#     b+= 'HTTP/1.0'
# elif a.raw.version==9:
#     b +=  'HTTP/0.9'
# elif a.raw.version==11:
#     b += 'HTTP/1.1'
# b+=" "+str(a.raw.status)+" "+str(a.raw.reason+"\n")+str(a.raw._fp.msg) + a.text
# print(b)

