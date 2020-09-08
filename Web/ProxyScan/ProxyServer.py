from mitmproxy import http
from mitmproxy import ctx
# from Web.Workbench.Tasks import printrmationLeakage
# from Web.WebClassCongregation import ProxyScanList
# from Web.WebClassCongregation import OriginalProxyData
class MitmproxyDataProcessing:
    def request(self, flow: http.HTTPFlow):
        self.RequestUrl = flow.request.url  # 完整的url
        self.RequestHeaders = {}  # 请求头数据
        for i in flow.request.headers:  # 对数据进行处理后存储到RequestHeaders中
            self.RequestHeaders.update({i: flow.request.headers[i]})
        self.RequestMethod = flow.request.method  # 请求方式
        self.RequestDate = ""  # 给Date赋值为空
        if self.RequestMethod == "POST":
            self.RequestDate = flow.request.get_text()  # 如果请求方式为POST，写入Date字段
        print(self.RequestUrl)
        print(self.RequestHeaders)
        print(self.RequestMethod)
        print(self.RequestDate)
        # print(str(flow.request.cookies))#cookies
        # print(flow.request.host)#域名 www.baidu.com
        # print(flow.request.method)#GET还是POST
        # print(flow.request.port)#请求端口
        # print(flow.request.scheme)#https还是http

    def response(self, flow: http.HTTPFlow):
        # print(flow.response.get_text())# 获取返回值结果 结果类型是字符串
        # print(flow.response.get_content()) #获取返回值结果 结果类型是bytes
        # print(flow.response.text) #获取返回值结果 结果类型是字符串
        # flow.response.set_text('123') #修改返回值 需要字符串类型
        self.ResponseDate = flow.response.content  # 获取返回值结果 结果类型是bytes二进制
        self.ResponseStatusCode = flow.response.status_code  # 状态码
        self.ResponseHeaders = {}  # 请求头数据
        for i in flow.response.headers:  # 对数据进行处理后存储到RequestHeaders中
            self.ResponseHeaders.update({i: flow.response.headers[i]})
        print(self.ResponseDate)
        print(self.ResponseStatusCode)
        print(self.ResponseHeaders)










