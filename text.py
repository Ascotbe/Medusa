# from config import headers,proxies
# medusa(Url="",ActiveScanId="Soryu Asuka Langley",Uid="Ayanami Rei",Headers=headers,Proxies=proxies)
# celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v0.82.3:palm_tree:"
# find . -type d -name '__pycache__' | xargs rm -rf
# pip install python-magic-bin==0.4.14
#-*-coding: UTF-8 -*-
import zipfile
import json
if __name__ == '__main__':
    zipFile = zipfile.ZipFile('/Users/ascotbe/Downloads/nvdcve-1.1-recent.json.zip', 'r')

    data = zipFile.read('nvdcve-1.1-recent.json').decode('utf-8')#读取到的byte类型进行转换到字符串类型
    ba=json.loads(data)["CVE_Items"]
    for i in ba:
        print(i)


    zipFile.close()