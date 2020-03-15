#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from OA.Weaver import WeaverCommandExecution
from OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(WeaverArbitraryFileDownloadVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(WeaverCommandExecution.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(WeaverDatabaseConfigurationInformationLeaked.medusa,Url,Values,UnixTimestamp)
    ThreadPool.Append(WeaverDatabaseConfigurationLeakVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(WeaveSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Weaver")