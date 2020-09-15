from mitmproxy import http
from mitmproxy import ctx
import base64
from Web.WebClassCongregation import ProxyScanList
from Web.WebClassCongregation import OriginalProxyData

def request(flow: http.HTTPFlow):
    RequestUrl = flow.request.url  # 完整的url
    RequestHeaders = {}  # 请求头数据
    for i in flow.request.headers:  # 对数据进行处理后存储到RequestHeaders中
        RequestHeaders.update({i: flow.request.headers[i]})
    RequestMethod = flow.request.method  # 请求方式
    RequestDate = ""  # 给Date赋值为空
    if RequestMethod == "POST":
        RequestDate = flow.request.get_text()  # 如果请求方式为POST，写入Date字段
    # print(RequestUrl)
    # print(RequestHeaders)
    # print(RequestMethod)
    # print(RequestDate)


    OriginalProxyData().Write(uid="test",oid="test",url=base64.b64encode(RequestUrl.encode(encoding="utf-8")),request_headers=base64.b64encode(str(RequestHeaders).encode(encoding="utf-8")),request_date=RequestMethod,request_method=base64.b64encode(RequestDate.encode(encoding="utf-8")))
    #header头解密函数eval(base64.b64decode(a).decode("utf-8"))
    # print(str(flow.request.cookies))#cookies
    # print(flow.request.host)#域名 www.baidu.com
    # print(flow.request.method)#GET还是POST
    # print(flow.request.port)#请求端口
    # print(flow.request.scheme)#https还是http










