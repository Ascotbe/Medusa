#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms版本探测
referer: unknow
author: Ascotbe
reference: Lucifer
description: 亿邮邮件系统存在弱口令账户信息泄露，导致非法登录
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

ver_histroy = {'20080307': 'v3 or v4 or v5',
		 '20080324': 'v5 above',
		 '20080807': '5.1 or 5.2',
		 '20081009': 'v5.1sp',
		 '20081218': '5.1sp',
		 '20090810': '5.5',
		 '20090912': '5.5',
		 '20100803': '5.6',
		 '20101021': '5.3',
		 '20111111': 'v5.7 or v5.6 or v5.5',
		 '20111205': '5.7.18',
		 '20111209': '5.6',
		 '20120430': '5.7SP or 5.7 or 5.6',
		 '20120621': '5.7SP1 or 5.7 or 5.6',
		 '20120709': '5.6',
		 '20121030': '5.7SP1 or 5.7',
		 '20121107': '5.7',
		 '20130608': 'V5.6-Final',
		 '20130922': 'V5.7SP1'}
payload = "/data/admin/ver.txt"
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
        con = re.search("^(\d+)$", resp.text)
        code = resp.status_code
        if con:
            Medusa = "{} 存在dedecms版本信息泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass