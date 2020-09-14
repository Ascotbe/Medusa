#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2019-9-19'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "OptionsMethodToOpenTheVulnerability" # 插件名称
        self.info['name'] ="Options方法开启漏洞" #漏洞名称
        self.info['affects'] = "无"  # 漏洞组件
        self.info['desc_content'] = "除了GET以及POST请求外还，开启了其他的请求方式，严重可以删除服务器任意文件。"  # 漏洞描述
        self.info['rank'] = "中危"  # 漏洞等级
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['suggest'] = "禁用其他方法，只留GET和POST"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url:str,Headers:dict,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    scheme, url, port = UrlProcessing().result(Url)
    try:
        payload_url = Url
        Headers["Accept-Language"] = "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
        Headers["Accept-Encoding"] = "gzip, deflate"

        resp = requests.options(payload_url,headers=Headers,proxies=proxies, timeout=5, verify=False)
        if r"OPTIONS" in resp.headers.get('Allow'):
            Medusa = "{}存在Options方法开启漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n漏洞详情:{}\r\n".format(url,payload_url,resp.headers)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类