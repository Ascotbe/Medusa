#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms._74CMS import _74CMSThereIsReflectiveXSSVulnerability
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists2
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists3
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists4
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists5
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists6
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists7
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists8
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists9
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists10
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists11
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists12
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists13
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists14
from Cms._74CMS import _74CMSSQLInjectionVulnerabilityExists15


import ClassCongregation
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [_74CMSThereIsReflectiveXSSVulnerability.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists2.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists3.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists4.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists5.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists6.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists7.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists8.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists9.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists10.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists11.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists12.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists13.medusa(Url,RandomAgent,ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists14.medusa(Url, RandomAgent, ProxyIp),
              _74CMSSQLInjectionVulnerabilityExists15.medusa(Url, RandomAgent, ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="74CMS plugin progress"):
            WriteFile.Write(str(i))
    except:
        pass