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
        self.info['algroup'] = "options"  # 插件名称
        self.info['name'] ='options方法开启漏洞' #漏洞名称
        self.info['affects'] = "http"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "只允许get以及post方法"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


def medusa(Url,RandomAgent,Token,proxies=None):
    proxies=ClassCongregation.Proxies().result(proxies)

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port

    try:
        payload_url = scheme+"://"+url+ ':' + str(port)
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        resp = requests.options(payload_url,headers=headers,proxies=proxies, timeout=5, verify=False)
        if r"OPTIONS" in resp.headers['Allow']:
            Medusa = "{}存在options方法开启漏洞 \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            _t = VulnerabilityInfo(Medusa)
            ClassCongregation.VulnerabilityDetails(_t.info, url, Token).Write()  # 传入url和扫描到的数据
            ClassCongregation.WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
