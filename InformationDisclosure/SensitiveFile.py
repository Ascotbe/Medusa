#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
import urllib3
urllib3.disable_warnings()
import urllib.parse
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "SensitiveFile"  # 插件名称
        self.info['name'] ='敏感文件压缩下载漏洞' #漏洞名称
        self.info['affects'] = ""  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['details'] = Medusa  # 结果
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

def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    Medusas=[]
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
                payload_url = scheme+"://"+url+ ':' + str(port)+payload+suffix

                headers = {
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'User-Agent': RandomAgent,
                }
                #s = requests.session()
                resp = requests.head(payload_url,headers=headers, timeout=5, verify=False)
                resp2 = requests.get(payload_url, headers=headers, timeout=5, verify=False)
                code = resp.status_code
                if code==200 and (resp2.headers["Content-Type"] == "application/zip" or resp2.headers["Content-Type"] == "application/x-rar-compressed" or resp2.headers["Content-Type"] == "application/x-gzip" or resp2.headers["Content-Type"] == "application/gzip") :
                    Medusa = "{} 存在敏感文件压缩下载漏洞\r\n漏洞详情:\r\nPayload:".format(payload_url)
                    Medusas.append(str(Medusa))
            except Exception as e:
                pass
    for Special in SpecialPayload:
        try:
            payload_url = scheme + "://" + url +':' + str(port)+ Special

            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            # s = requests.session()
            resp = requests.head(payload_url, headers=headers, timeout=5, verify=False)
            resp2 = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            code = resp.status_code
            if code == 200 and resp2.headers["Content-Type"] == "text/plain":
                Medusa = "{} 存在敏感文件压缩下载漏洞\r\n漏洞详情:\r\nPayload:".format(payload_url)
                Medusas.append(str(Medusa))
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
                return (_t.info)
        except:
            _ = VulnerabilityInfo('').info.get('algroup')
            _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类

    Medusas_str = ''
    for i in Medusas:
        Medusas_str = Medusas_str + i
    return (str(Medusas_str))