#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import OA.Weaver.Weaver_db_disclosure
import OA.Weaver.Weaver_sqli
import OA.Weaver.Weaver_filedownload
import OA.Weaver.Weaver_CommandExecution
import OA.Weaver.Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability
import ClassCongregation


def Main(Url, FileName, Values, ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua = ClassCongregation.UserAgentS(Values)  # 传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件
    try:
        Medusa = OA.Weaver.Weaver_db_disclosure.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa = OA.Weaver.Weaver_sqli.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa = OA.Weaver.Weaver_filedownload.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa = OA.Weaver.Weaver_CommandExecution.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa = OA.Weaver.Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass