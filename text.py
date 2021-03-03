# from config import headers,proxies
# medusa(Url="",ActiveScanId="Soryu Asuka Langley",Uid="Ayanami Rei",Headers=headers,Proxies=proxies)
# celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v0.82.3:palm_tree:"
# find . -type d -name '__pycache__' | xargs rm -rf
# pip install python-magic-bin==0.4.14

import time
StartingTime=time.time()+1
ZipFilePath="11111"
ExtractData=["d","ss"]
FileName="dasdasd"
print("[ + ] 下载文件：\033[36m" + FileName + "\033[0m 耗时：\033[34m" + str(
    time.time() - StartingTime) + "S \033[0m")
print("[ ~ ] 本次写入文件：\033[36m" + ZipFilePath + "\033[0m 耗时：\033[34m" + str(
    time.time() - StartingTime) + "S \033[0m 数据量：\033[32m" + str(len(ExtractData)) + "\033[0m条")
print("[ - ] 正在重新下载文件：\033[36m" + FileName + "\033[0m 耗时：\033[34m" + str(
    time.time() - StartingTime) + "S \033[0m")

