from mitmproxy import http
import base64
import time
from config import agent_scan_interval
from Web.Workbench.Tasks import ProxyScan
from ClassCongregation import Md5Encryption
import re
from Web.WebClassCongregation import ProxyScanList,OriginalProxyData,ProxyTempUrl
class ProxyDataCollection(object):

    def authenticate(self, flow: http.HTTPFlow):
        self.Auth = flow.metadata.get('proxyauth')
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
        if not self.Auth:
            flow.response.set_text("请进行代理认证")#修改返回值 需要字符串类型
            return 0
        else:
            self.Username, self.Password = self.Auth
        #账号密码认证
        self.request(flow)
        self.ResponseDateString = flow.response.text #获取返回值结果 结果类型是字符串
        self.ResponseDateBytes = flow.response.content  # 获取返回值结果 结果类型是bytes二进制
        self.ResponseStatusCode = flow.response.status_code  # 状态码
        self.ResponseHeaders = {}  # 请求头数据
        for i in flow.response.headers:  # 对数据进行处理后存储到RequestHeaders中
            self.ResponseHeaders.update({i: flow.response.headers[i]})
        self.Md5Password=Md5Encryption().Md5Result(self.Password)#对密码进行MD5加密


        ProxyAuthenticationResult=ProxyScanList().ProxyAuthentication(proxy_username=self.Username,proxy_password=self.Md5Password)#对数据进行校检
        if ProxyAuthenticationResult==None:
            flow.response.set_text("账号或密码错误~")  # 认证失败
            return 0
        else:
            #进行判断的ProxyTempUrl类使用判断的URL是正则处理过的，而记录到OriginalProxyData类中的URL是未处理过的
            RequestUrl=str(bytes.decode(self.RequestUrl.encode(encoding="utf-8")))#转换成字符型
            try:
                UrlRegularMatchingProcessing=re.search(r'http[s]?://(.*)?/', RequestUrl, re.I).group(0)#对URL进行提取处理
                if UrlRegularMatchingProcessing!=None:#进行判断匹配结果

                    ScanExecutionTime=ProxyTempUrl().Query(uid=ProxyAuthenticationResult["uid"],proxy_temp_url=UrlRegularMatchingProcessing,proxy_id=ProxyAuthenticationResult["proxy_id"])#先进行查询如果查到数据进行时间匹配
                    if ScanExecutionTime==None:#表示没有数据
                        RedisTask= ProxyScan.delay(UrlRegularMatchingProcessing,bytes.decode(str(self.RequestHeaders).encode(encoding="utf-8")),Uid=ProxyAuthenticationResult["uid"],ActiveScanId="0")#由于代理扫描没有ActiveScanId值所以全局使用0
                        OriginalProxyData().Write(uid=ProxyAuthenticationResult["uid"],proxy_id=ProxyAuthenticationResult["proxy_id"],url=RequestUrl,request_headers=base64.b64encode(str(self.RequestHeaders).encode(encoding="utf-8")),request_date=self.RequestMethod,request_method=base64.b64encode(self.RequestDate.encode(encoding="utf-8")),
                                              response_headers=str(self.ResponseHeaders).encode(encoding="utf-8"),response_status_code=self.ResponseStatusCode,response_date_string=self.ResponseDateString.encode(encoding="utf-8"),response_date_bytes=str(self.ResponseDateBytes).encode(encoding="utf-8"),redis_id=RedisTask.task_id)
                        ProxyTempUrl().Write(uid=ProxyAuthenticationResult["uid"],redis_id=RedisTask.task_id,proxy_temp_url=UrlRegularMatchingProcessing,proxy_id=ProxyAuthenticationResult["proxy_id"])
                    else:#有数据的话进行计算
                        TimeDifferencestr=int(time.time())-int(ScanExecutionTime)#计算时间差
                        if TimeDifferencestr>agent_scan_interval:#如果间隔超过定义时间就从新下发到任务中
                            RedisTask = ProxyScan.delay(UrlRegularMatchingProcessing,
                                                        bytes.decode(str(self.RequestHeaders).encode(encoding="utf-8")),
                                                        Uid=ProxyAuthenticationResult["uid"],
                                                        ActiveScanId="0")  # 由于代理扫描没有ActiveScanId值所以全局使用0
                            OriginalProxyData().Write(uid=ProxyAuthenticationResult["uid"],
                                                      proxy_id=ProxyAuthenticationResult["proxy_id"], url=RequestUrl,
                                                      request_headers=base64.b64encode(
                                                          str(self.RequestHeaders).encode(encoding="utf-8")),
                                                      request_date=self.RequestMethod, request_method=base64.b64encode(
                                    self.RequestDate.encode(encoding="utf-8")),
                                                      response_headers=str(self.ResponseHeaders).encode(encoding="utf-8"),
                                                      response_status_code=self.ResponseStatusCode,
                                                      response_date_string=self.ResponseDateString.encode(encoding="utf-8"),
                                                      response_date_bytes=str(self.ResponseDateBytes).encode(encoding="utf-8"),
                                                      redis_id=RedisTask.task_id)
                            ProxyTempUrl().Write(uid=ProxyAuthenticationResult["uid"], redis_id=RedisTask.task_id,
                                                 proxy_temp_url=UrlRegularMatchingProcessing, proxy_id=ProxyAuthenticationResult["proxy_id"])
            except Exception as e:
                pass


addons = [
    ProxyDataCollection()
]