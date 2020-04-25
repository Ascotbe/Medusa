from mitmproxy import ctx
from Web.api.tasks import InformationLeakage
def request(flow):
    RequestProxy= flow.request
    if RequestProxy.url!=None:
        InformationLeakage.delay(RequestProxy.url,"test",2000,None)





    # info = ctx.log.info
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