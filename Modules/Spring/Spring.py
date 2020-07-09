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
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(SpringReflectionFileDownloadVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringPathTraversalVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringPathTraversalVulnerability2.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringBootFrameworkSPELExpressionInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringBootH2DatabaseJNDIInjection.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringSecurityOauth2RemoteCodeExecution.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SpringDataCommonsRemoteCommandExecutionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Spring")
