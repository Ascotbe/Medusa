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
from Web.WebClassCongregation import NistData
import json
# print(json.dumps(NistData().BulkQuery(number_of_pages=500)))
# print(NistData().StatisticalData())
# print(NistData().DetailedQuery(common_vulnerabilities_and_exposures="CVE-2019-18243"))
print(NistData().VendorsQuery(number_of_pages=0,vendors="Haxx"))
print(NistData().ModuleDataStatistics(module_name="v3_base_severity",module_content="HIGH"))
print(NistData().ModuleDataStatistics(module_name="vendors",module_content="%Haxx%"))
print(NistData().ModuleDataStatistics(module_name="products",module_content="%Curl%"))

