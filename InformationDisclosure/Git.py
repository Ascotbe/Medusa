#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "Git_version_management_source_leak_vulnerability"  # 插件名称
        self.info['name'] ='Git版本管理源码泄露漏洞' #漏洞名称
        self.info['affects'] = "Git"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


list= ['80','443','8080','8443','8081','9008','81']
ReturnList=[]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        if str(port) not in list:
            list.append(str(port))#如果列表中不存在用户输入的端口，就把该端口发送到list里面下面好利用扫描
    global   resp
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    for payload in list:
        PayloadUrl =scheme + '://' + url + ':' + payload+'/.git/config'
        try:
            s = requests.session()
            resp = s.get(PayloadUrl,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('repositoryformatversion')!=-1 :
                Medusa = "{} 存在Git版本管理源码泄露漏洞\r\n漏洞详情:{}\r\n".format(url, PayloadUrl)
                ReturnList.append(Medusa)
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
        except:
            _ = VulnerabilityInfo('').info.get('algroup')
            _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
    Medusas_str = ''
    for i in ReturnList:
        Medusas_str = Medusas_str + i
    return (str(Medusas_str))


