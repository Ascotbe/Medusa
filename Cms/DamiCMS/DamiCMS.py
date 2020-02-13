#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability1
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability2
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability3
from ClassCongregation import WriteFile,UserAgentS
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFiles = WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [DamiCMSSQLInjectionVulnerability1.medusa(Url,RandomAgent,ProxyIp),
              DamiCMSSQLInjectionVulnerability2.medusa(Url, RandomAgent, ProxyIp),
              DamiCMSSQLInjectionVulnerability3.medusa(Url, RandomAgent, ProxyIp),
              ]
    try:
        for i in tqdm(Medusa, ascii=True, desc="DamiCMS plugin progress"):
            WriteFiles.Write(str(i))
    except:
        pass