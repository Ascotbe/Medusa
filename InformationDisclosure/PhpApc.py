
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import requests
import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "phpapc"  # 插件名称
        self.info['name'] ='php_apc缓存页面信息泄露漏洞' #漏洞名称
        self.info['affects'] = "phpapc"  # 漏洞组件
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


list= ['/', '/admin', '/common', '/customer', '/code', '/edm', '/info', '/job', '/kefu', '/ROOT', '/upload', '/sale','/video', '/WEB-INF', '/WeChat', '/server', '/MSSH5']
ReturnList=[]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    for payload in list:
        PayloadUrl = url + ':' + str(port)+payload+'/apc.php'
        try:
            s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = s.get(PayloadUrl, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = s.get(PayloadUrl,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('apc version')!=-1:
                Medusa = "{} \r\n漏洞详情:{}\r\n".format(url, PayloadUrl)
                ReturnList.append(Medusa)
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
                return (_t.info)
        except:
            logging.warning(Url)
            _ = VulnerabilityInfo('')
            logging.warning(_.info.get('parameter'))
    _t = VulnerabilityInfo(ReturnList)
    return (_t.info)


