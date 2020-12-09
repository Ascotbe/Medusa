#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Weaver import WeaverArbitraryFileDownloadVulnerability
from Modules.OA.Weaver import WeaverCommandExecution
from Modules.OA.Weaver import WeaverDatabaseConfigurationInformationLeaked
from Modules.OA.Weaver import WeaverDatabaseConfigurationLeakVulnerability
from Modules.OA.Weaver import WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability
from Modules.OA.Weaver import WeaveSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(WeaverArbitraryFileDownloadVulnerability.medusa,** kwargs)
    Pool.Append(WeaverCommandExecution.medusa, ** kwargs)
    Pool.Append(WeaverDatabaseConfigurationInformationLeaked.medusa,** kwargs)
    Pool.Append(WeaverDatabaseConfigurationLeakVulnerability.medusa,** kwargs)
    Pool.Append(WeaverWorkflowCenterTreeDataInterfaceInjectionVulnerability.medusa, ** kwargs)
    Pool.Append(WeaveSQLInjectionVulnerability.medusa, ** kwargs)
    Prompt("Weaver")