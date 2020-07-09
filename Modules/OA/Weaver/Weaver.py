#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from Modules.OA.Weaver import WeaverCommandExecution
from Modules.OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from Modules.OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from Modules.OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from Modules.OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(WeaverArbitraryFileDownloadVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WeaverCommandExecution.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WeaverDatabaseConfigurationInformationLeaked.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WeaverDatabaseConfigurationLeakVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WeaveSQLInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Weaver")