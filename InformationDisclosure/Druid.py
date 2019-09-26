#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


list = ['/index.html','/datasource.html','/sql.html','/wall.html','/webapp.html','/weburi.html','/websession.html','/spring.html']
ReturnList=[]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    for payload in list:
        PayloadUrl = url + ':' + str(port)+'/druid'+payload
        try:
            s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = s.get(PayloadUrl, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = s.get(PayloadUrl,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('druid.common')!=-1:
                Medusa = "{} 存在Druid监控系统泄露漏洞\r\n漏洞详情:{}\r\n".format(url, PayloadUrl)
                ReturnList.append(Medusa)
        except Exception as e:
            pass
    return (ReturnList)
