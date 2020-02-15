#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from OA.Weaver import WeaverCommandExecution
from OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import WriteFile,UserAgentS
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFiles = WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件
    Medusa = [WeaverArbitraryFileDownloadVulnerability.medusa(Url, RandomAgent, ProxyIp),
              WeaverCommandExecution.medusa(Url, RandomAgent, ProxyIp),
              WeaverDatabaseConfigurationInformationLeaked.medusa(Url, RandomAgent, ProxyIp),
              WeaverDatabaseConfigurationLeakVulnerability.medusa(Url, RandomAgent, ProxyIp),
              WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp),
              WeaveSQLInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Weaver plugin progress"):
            WriteFiles.Write(str(i))
    except:
        pass
