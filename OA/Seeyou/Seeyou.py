#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import OA.Seeyou.Seeyou_a8_logs_disclosure
import OA.Seeyou.Seeyou_cm_info_content_sqli
import OA.Seeyou.Seeyou_ehr_ELTextFile
import OA.Seeyou.Seeyou_fe_treeXml_sqli
import OA.Seeyou.Seeyou_getemaildata_fileread
import OA.Seeyou.Seeyou_icc_struts2
import OA.Seeyou.Seeyou_multi_union_sqli
import OA.Seeyou.Seeyou_NCFindWeb_fileread
import OA.Seeyou.Seeyou_status_default_pwd
import OA.Seeyou.Seeyou_test_sqli
import OA.Seeyou.Seeyou_user_ids_sqli
import ClassCongregation


def Main(Url, FileName, Values, ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua = ClassCongregation.UserAgentS(Values)  # 传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件

    try:
        Medusa =OA.Seeyou.Seeyou_a8_logs_disclosure.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_cm_info_content_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_ehr_ELTextFile.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa =OA.Seeyou.Seeyou_fe_treeXml_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_getemaildata_fileread.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_icc_struts2.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa =OA.Seeyou.Seeyou_multi_union_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_NCFindWeb_fileread.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_status_default_pwd.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa =OA.Seeyou.Seeyou_test_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa =OA.Seeyou.Seeyou_user_ids_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass


