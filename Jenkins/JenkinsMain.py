#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Jenkins import JenkinsArbitraryFileReadVulnerability
from Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import WriteFile,UserAgentS
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFiles = WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [JenkinsArbitraryFileReadVulnerability.medusa(Url,RandomAgent,ProxyIp),JenkinsRemoteCommandExecutionVulnerability.medusa(Url,RandomAgent,ProxyIp),JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa(Url,RandomAgent,ProxyIp)]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Jenkins plugin progress"):
            WriteFiles.Write(str(i))
    except:
        pass



