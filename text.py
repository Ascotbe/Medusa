# !/usr/bin/env python
# -*- coding: utf-8 -*-
# if __name__ == '__main__':
#     UrlList=[]
#     ThredList=[]
#     with open("123.txt", 'r', encoding='UTF-8') as f:
#         line = f.readline()
#         while line:
#             ThredList.append(threading.Thread(target=audit, args=(line.strip("\r\n",),"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")))
#             line = f.readline()
# medusa("","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")
#find . -type d -name '__pycache__' | xargs rm -rf
import ClassCongregation
#ClassCongregation.AccountInquiry("ttttt").Inquire()
#ClassCongregation.Register().Write("aaa","2222","25@qq.com","1111111")
aa=ClassCongregation.UserTable().CheckUserToken("1111111")
print(aa)