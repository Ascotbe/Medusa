#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2019-9-19'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "SvnVersionManagementSourceCodeLeakVulnerability" # 插件名称
        self.info['name'] ="Svn版本管理源码泄露漏洞" #漏洞名称
        self.info['affects'] = "Svn"  # 漏洞组件
        self.info['desc_content'] = "敏感文件未删除，导致用户可以访问或者下载，造成大量的数据或源码泄露。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url:str,RandomAgent:str,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    try:
        payload = '/.svn/entries'
        payload_url = Url+ payload
        headers = {
            'User-Agent': RandomAgent,
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }
        resp = requests.get(payload_url,headers=headers, proxies=proxies, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code==200 and  con.lower().find('svn://')!=-1:
            Medusa = "{} 存在Svn版本管理源码泄露漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n漏洞详情:{}\r\n".format(Url,payload_url,con)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, Url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(Url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+Url,e)#调用写入类