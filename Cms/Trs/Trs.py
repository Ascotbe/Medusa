#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Cms.Trs.Trs_ids_auth_disclosure
import Cms.Trs.Trs_infogate_register
import Cms.Trs.Trs_inforadar_disclosure
import Cms.Trs.Trs_lunwen_papercon_sqli
import Cms.Trs.Trs_was5_config_disclosure
import Cms.Trs.Trs_was5_download_templet
import Cms.Trs.Trs_was40_passwd_disclosure
import Cms.Trs.Trs_wcm_default_user
import Cms.Trs.Trs_wcm_infoview_disclosure
import Cms.Trs.Trs_wcm_pre_as_lfi
import Cms.Trs.Trs_wcm_service_writefile
import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Cms.Trs.Trs_ids_auth_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Trs.Trs_infogate_register.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Trs.Trs_inforadar_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =Cms.Trs.Trs_lunwen_papercon_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa=Cms.Trs.Trs_was5_config_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =Cms.Trs.Trs_was5_download_templet.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa=Cms.Trs.Trs_was40_passwd_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa =Cms.Trs.Trs_wcm_default_user.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =Cms.Trs.Trs_wcm_infoview_disclosure.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =Cms.Trs.Trs_wcm_pre_as_lfi.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =Cms.Trs.Trs_wcm_service_writefile.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass