#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Spring import SpringReflectionFileDownloadVulnerability
from Modules.Spring import SpringPathTraversalVulnerability
from Modules.Spring import SpringPathTraversalVulnerability2
from Modules.Spring import SpringBootFrameworkSPELExpressionInjectionVulnerability
from Modules.Spring import SpringBootH2DatabaseJNDIInjection
from Modules.Spring import SpringSecurityOauth2RemoteCodeExecution
from Modules.Spring import SpringDataCommonsRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(SpringReflectionFileDownloadVulnerability.medusa,** kwargs)
    Pool.Append(SpringPathTraversalVulnerability.medusa,** kwargs)
    Pool.Append(SpringPathTraversalVulnerability2.medusa, ** kwargs)
    Pool.Append(SpringBootFrameworkSPELExpressionInjectionVulnerability.medusa, ** kwargs)
    Pool.Append(SpringBootH2DatabaseJNDIInjection.medusa,** kwargs)
    Pool.Append(SpringSecurityOauth2RemoteCodeExecution.medusa,** kwargs)
    Pool.Append(SpringDataCommonsRemoteCommandExecutionVulnerability.medusa,** kwargs)
    Prompt("Spring")
