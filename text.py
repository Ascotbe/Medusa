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

ZipFilePath="/Users/ascotbe/code/Medusa/Temp/nvdcve-1.1-2002.json.zip"
print("[ + ] 初始化文件失败正在重新下载：\033[36m" +ZipFilePath[-13:-9]+ "dasda"+ZipFilePath[:-24]+"\033[0m")