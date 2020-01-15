#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.B2Bbuilder import B2BbuilderBackgroundCommandExecutionVulnerability
from Cms.B2Bbuilder import B2BbuilderContainsVulnerabilitiesLocally
from Cms.B2Bbuilder import B2BbuilderHeadSQLInjectionVulnerability
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability2
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability3
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability4


import ClassCongregation
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [B2BbuilderBackgroundCommandExecutionVulnerability.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderContainsVulnerabilitiesLocally.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderHeadSQLInjectionVulnerability.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderSQLInjectionVulnerability.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderSQLInjectionVulnerability2.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderSQLInjectionVulnerability3.medusa(Url,RandomAgent,ProxyIp),
              B2BbuilderSQLInjectionVulnerability4.medusa(Url,RandomAgent,ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="B2Bbuilder plugin progress"):
            WriteFile.Write(str(i))
    except:
        pass