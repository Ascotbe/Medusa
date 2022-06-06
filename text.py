# celery -A Web worker -B --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# 测试启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# pip install python-magic-bin==0.4.14
a={
		"信息安全": ["ascotbe@gmail.com", "ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"],
		"客服": ["1099482542@qq.com"]
	}

import json
for i in a:
	for x in a[i]:
		print(x)

