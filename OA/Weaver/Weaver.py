#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Weaver import Weaver_db_disclosure
from OA.Weaver import Weaver_sqli
from OA.Weaver import Weaver_filedownload
from OA.Weaver import Weaver_CommandExecution
from OA.Weaver import Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability
import ClassCongregation
from tqdm import tqdm

def Main(Url, FileName, Values, ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua = ClassCongregation.UserAgentS(Values)  # 传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件
    Weaver_db_disclosure.medusa(Url, RandomAgent, ProxyIp),Weaver_sqli.medusa(Url, RandomAgent, ProxyIp),Weaver_filedownload.medusa(Url, RandomAgent, ProxyIp),Weaver_CommandExecution.medusa(Url, RandomAgent, ProxyIp),Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp),
    Medusa = [Weaver_db_disclosure.medusa(Url, RandomAgent, ProxyIp),Weaver_sqli.medusa(Url, RandomAgent, ProxyIp),Weaver_filedownload.medusa(Url, RandomAgent, ProxyIp),Weaver_CommandExecution.medusa(Url, RandomAgent, ProxyIp),Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa(Url, RandomAgent, ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Weaver plugin progress:"):
            WriteFile.Write(str(i))
    except:
        pass
