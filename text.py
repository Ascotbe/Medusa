# celery -A Web worker -B --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# 测试启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# pip install python-magic-bin==0.4.14
# def read_bigFile():
#     c=""
#     ix=0
#     f=open("/Users/ascotbe/Desktop/x86.txt", 'rb')
#     w = open("/Users/ascotbe/Desktop/2.txt", 'a+')
#     while True:
#         ix+=1
#         data = f.read(1)
#         if not data: break
#         #print(data.hex())
#         c += "\\x" + data.hex()
#         if ix==30:
#             w.write("\""+c+"\"\n")
#             ix=0
#             c=""
#     if c!=None:
#         w.write("\"" + c + "\"\n")
#     w.close()
#     f.close()
# read_bigFile()