#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import SeeyouArbitraryFileReadVulnerability
from OA.Seeyou import SeeyouMultipleSQLInjectionVulnerabilities
from OA.Seeyou import SeeyouOALogInformationDisclosureVulnerability
from OA.Seeyou import SeeyouSeeyouSystemFileArbitraryReadVulnerability2
from OA.Seeyou import SeeyouSQLInjectionVulnerability2
from OA.Seeyou import SeeyouSQLInjectionVulnerability3
from OA.Seeyou import SeeyouStatusDefaultPwdVulnerability
from OA.Seeyou import SeeyouSystemFileArbitraryReadVulnerability
from OA.Seeyou import SeeyouSystemFrameworkVulnerability
from OA.Seeyou import SeeyouSystemSQLInjectionVulnerability
from ClassCongregation import WriteFile,UserAgentS
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFiles = WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件

    Medusa = [SeeyouArbitraryFileReadVulnerability.medusa(Url, RandomAgent, ProxyIp),
              SeeyouMultipleSQLInjectionVulnerabilities.medusa(Url, RandomAgent, ProxyIp),
              SeeyouOALogInformationDisclosureVulnerability.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSeeyouSystemFileArbitraryReadVulnerability2.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSQLInjectionVulnerability2.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSQLInjectionVulnerability3.medusa(Url, RandomAgent, ProxyIp),
              SeeyouStatusDefaultPwdVulnerability.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSystemFileArbitraryReadVulnerability.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSystemFrameworkVulnerability.medusa(Url, RandomAgent, ProxyIp),
              SeeyouSystemSQLInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Seeyou plugin progress"):
            WriteFiles.Write(str(i))
    except:
        pass

