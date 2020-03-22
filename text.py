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
import base64
import re
a=ClassCongregation.BotVulnerabilityInquire("e4f16eed8fa82e84886bd4ab34d99dc5").Inquire()
def JsonProcessing():#对返回的json进行处理
    a="Token:e4f16eed8fa82e84886bd4ab34d99dc5\r\nKey:1584860852"
    regular_match_results = re.search(r'Token:([\w\u4e00-\u9fa5!@#$%^*()&-=+_`~/?.,<>\\|\[\]{}]*)',a).group(1)
    print(regular_match_results)
    c = re.search(r'Key:([\w\u4e00-\u9fa5!@#$%^*()&-=+_`~/?.,<>\\|\[\]{}]*)',a).group(1)
    print(c)
JsonProcessing()