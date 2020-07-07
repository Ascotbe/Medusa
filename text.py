# !/usr/bin/env python
# -*- coding: utf-8 -*-
# if __name__ == '__main__':
#     UrlList=[]
#     ThredList=[]
#     la=[]
#     with open("6.txt", 'r', encoding='UTF-8') as f:
#         line = f.readline()
#         while line:
#             ThredList.append(threading.Thread(target=medusa, args=(line.strip("\r\n",),"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",),kwargs={"Uid":"Ayanami Rei","Sid":"Soryu Asuka Langley"}))
#             line = f.readline()
#     for t in ThredList:  # 开启列表中的多线程
#         t.start()
#     for p in ThredList:  # 开启列表中的多线程
#         p.join()
# medusa("","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")
#celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
#python3 manage.py runserver 0.0.0.0:9999
#.\redis-server.exe redis.windows.conf
# git commit -m  "v0.82.3:palm_tree:"
#find . -type d -name '__pycache__' | xargs rm -rf