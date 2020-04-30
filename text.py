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
# import mitmproxy.http
# import mitmproxy.ctx
# from Web.api.tasks import InformationLeakage
# def request(flow: mitmproxy.http.HTTPFlow)->None:
#     try:
#         RequestProxy= flow.request
#         auth=flow.metadata.get("proxyauth")
#         if auth[0] =="" or auth[1] =="":
#             print("nb")
#             RequestProxy.host = "medusa.ascotbe.com"
#         print(auth[0])
#         print(auth[1])
#         print(type(auth))
#     except:pass


    # if RequestProxy.url!=None:
    #     InformationLeakage.delay(RequestProxy.url,"test",2000,None)
    # info = mitmproxy.ctx.log.info
    # info(RequestProxy.url)# 完整的url  https://www.baidu.com/
    # info(str(RequestProxy.headers))#请求头
    # info(str(RequestProxy.cookies))#cookies
    # info(RequestProxy.host)#域名 www.baidu.com
    # info(RequestProxy.method)#GET还是POST
    # info(str(RequestProxy.port))#请求端口
    # info(RequestProxy.scheme)#https还是http


# def response(flow):
#     response = flow.response
#     info = ctx.log.info
#     info(str(response.status_code))
#     info(str(response.headers))
#     info(str(response.cookies))
#     info(str(response.text))