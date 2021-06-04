import celpy
import yaml
from config import headers
#找一个能获取完整request数据的请求包
#怎么使用cel
#如何处理多个请求
#哪些参数是固定的
#当存在post和get的时候区分
#有其他参数不确定的参数怎么处理

def qu(url):
    YamlFile="/Users/ascotbe/code/Medusa/Plugins/test.yaml"
    YamlData=yaml.full_load(open(YamlFile,"r+"))
    YamlRules=YamlData.get("rules")
    YamlDetail=YamlData.get("detail")
    YamlName=YamlData.get("name")
    print(YamlRules)
    print(YamlDetail)
    print(YamlName)

    Headers=headers
    for i in YamlRules[0]["headers"]:
        Headers[i]=YamlRules[0]["headers"][i]
    print(Headers)

qu("dasd")
import HackRequests
# def t():
#     url="http://127.0.0.1:8000/a"
#     hack=HackRequests.hackRequests()
#     b=hack.http(url, headers=headers,method="HEAD",location=True,proxy=('127.0.0.1','8080'),cookie={},referer="")
#     print(b.log.get("request"))
#     print()
#     print(b.log.get("response"))

# t()
