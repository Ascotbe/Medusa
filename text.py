# from config import headers,proxies
# medusa(Url="",ActiveScanId="Soryu Asuka Langley",Uid="Ayanami Rei",Headers=headers,Proxies=proxies)
# celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
'''openssl自签名
openssl genrsa -des3 -out server.key 2048
openssl req -new -key server.key -out server.csr -config openssl.cnf
openssl rsa -in server.key -out server_no_passwd.key
openssl x509 -req -days 365 -in server.csr -signkey server_no_passwd.key -out server.crt
'''
# 启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# find . -type d -name '__pycache__' | xargs rm -rf
# pip install python-magic-bin==0.4.14