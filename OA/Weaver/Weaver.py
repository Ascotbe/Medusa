#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from OA.Weaver import WeaverCommandExecution
from OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(WeaverArbitraryFileDownloadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(WeaverCommandExecution.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(WeaverDatabaseConfigurationInformationLeaked.medusa,Url,Values,Token,proxies=proxies)
    ThreadPool.Append(WeaverDatabaseConfigurationLeakVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(WeaveSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Weaver")