from ClassCongregation import UrlProcessing
import ClassCongregation
a=UrlProcessing().result("www.baidu.com:8081")
ClassCongregation.UrlProcessing().result("www.baidu.com:8081")
scheme, url, port = a
print(scheme)
print(url,port)