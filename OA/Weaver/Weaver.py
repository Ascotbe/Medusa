#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from OA.Weaver import WeaverCommandExecution
from OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(WeaverArbitraryFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(WeaverCommandExecution.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(WeaverDatabaseConfigurationInformationLeaked.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(WeaverDatabaseConfigurationLeakVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(WeaveSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Weaver")