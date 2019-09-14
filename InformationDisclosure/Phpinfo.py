
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


list = [
    '/index.php',
    '/1.php',
    '/2.php',
    '/3.php',
    '/4.php',
    '/5.php',
    '/6.php',
    '/7.php',
    '/8.php',
    '/9.php',
    '/10.php',
    '/11.php',
    '/12.php',
    '/13.php',
    '/123.php',
    '/1234.php',
    '/12345.php',
    '/123456.php',
    '/a.php',
    '/b.php',
    '/c.php',
    '/d.php',
    '/e.php',
    '/f.php',
    '/g.php',
    '/h.php',
    '/i.php',
    '/j.php',
    '/k.php',
    '/l.php',
    '/m.php',
    '/n.php',
    '/o.php',
    '/p.php',
    '/q.php',
    '/r.php',
    '/s.php',
    '/t.php',
    '/u.php',
    '/v.php',
    '/w.php',
    '/x.php',
    '/y.php',
    '/z.php',
    '/php.php',
    '/abc.php',
    '/test.php',
    '/test1.php',
    '/test2.php',
    '/test3.php',
    '/test123.php',
    '/2013/test.php',
    '/2014/test.php',
    '/2015/test.php',
    '/info.php',
    '/phpinfo.php',
    '/iProber.php',
    '/iProber1.php',
    '/iProber2.php',
    '/iProber3.php',
    '/test_phpinfo.php',
    '/tools/info.php',
    '/ship/phpinfo.php',
    '/web/info.php',
    '/web/phpinfo.php',
    '/xampp/info.php',
    '/xampp/phpinfo.php',
    '/index.php?act=phpinfo',
    '/dashboard/phpinfo.php'
]
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
        PayloadUrl = url + ':' + str(port)+payload
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
            if code==200 and con.lower().find('<title>phpinfo()</title>')!=-1:
                Medusa = "{} 存在phpinfo测试脚本泄露漏洞\r\n漏洞详情:{}\r\n".format(url, PayloadUrl)
                ReturnList.append(Medusa)
        except Exception as e:
            pass
    return (ReturnList)



