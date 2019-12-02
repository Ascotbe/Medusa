#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Cms.Dedecms.Dedecms_download_redirect
import Cms.Dedecms.Dedecms_error_trace_disclosure
import Cms.Dedecms.Dedecms_recommend_sqli
import Cms.Dedecms.Dedecms_search_typeArr_sqli
import Cms.Dedecms.Dedecms_version
import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Cms.Dedecms.Dedecms_download_redirect.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Dedecms.Dedecms_error_trace_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Dedecms.Dedecms_recommend_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa = Cms.Dedecms.Dedecms_search_typeArr_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=Cms.Dedecms.Dedecms_version.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass