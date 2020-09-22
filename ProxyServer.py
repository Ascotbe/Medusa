from mitmproxy import http
import base64
from Web.WebClassCongregation import ProxyScanList
from Web.WebClassCongregation import OriginalProxyData
class ProxyDataCollection(object):

    def authenticate(self, flow: http.HTTPFlow):
        self.auth = flow.metadata.get('proxyauth')
        #self.sourceip = flow.client_conn.ip_address[0]

    def request(self,flow: http.HTTPFlow):
        self.RequestUrl = flow.request.url  # 完整的url
        self.RequestHeaders = {}  # 请求头数据
        for i in flow.request.headers:  # 对数据进行处理后存储到RequestHeaders中
            self.RequestHeaders.update({i: flow.request.headers[i]})
        self.RequestMethod = flow.request.method  # 请求方式
        self.RequestDate = ""  # 给Date赋值为空
        if self.RequestMethod == "POST":
            self.RequestDate = flow.request.get_text()  # 如果请求方式为POST，写入Date字段
        #header头解密函数eval(base64.b64decode(a).decode("utf-8"))
    def response(self, flow: http.HTTPFlow):
        self.authenticate(flow)
        if not self.auth:
            flow.response.set_text("请进行代理认证")#修改返回值 需要字符串类型
            return 0
        else:
            self.username, self.password = self.auth
        #账号密码认证
        self.request(flow)
        self.ResponseDateString = flow.response.text #获取返回值结果 结果类型是字符串
        self.ResponseDateBytes = flow.response.content  # 获取返回值结果 结果类型是bytes二进制
        self.ResponseStatusCode = flow.response.status_code  # 状态码
        self.ResponseHeaders = {}  # 请求头数据
        for i in flow.response.headers:  # 对数据进行处理后存储到RequestHeaders中
            self.ResponseHeaders.update({i: flow.response.headers[i]})
        OriginalProxyData().Write(uid="test",sid="test",url=base64.b64encode(self.RequestUrl.encode(encoding="utf-8")),request_headers=base64.b64encode(str(self.RequestHeaders).encode(encoding="utf-8")),request_date=self.RequestMethod,request_method=base64.b64encode(self.RequestDate.encode(encoding="utf-8")),
                                  response_headers=str(self.ResponseHeaders).encode(encoding="utf-8"),response_status_code=self.ResponseStatusCode,response_date_string=self.ResponseDateString.encode(encoding="utf-8"),response_date_bytes=str(self.ResponseDateBytes).encode(encoding="utf-8"))
        # print(self.username, self.password)
        # print(self.ResponseDateString)
        # print(self.ResponseDateBytes)
        # print(self.ResponseStatusCode)
        # print(self.ResponseHeaders)

addons = [
    ProxyDataCollection()
]