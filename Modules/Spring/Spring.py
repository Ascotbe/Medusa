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
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(SpringReflectionFileDownloadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SpringPathTraversalVulnerability.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SpringPathTraversalVulnerability2.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SpringBootFrameworkSPELExpressionInjectionVulnerability.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SpringBootH2DatabaseJNDIInjection.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SpringSecurityOauth2RemoteCodeExecution.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SpringDataCommonsRemoteCommandExecutionVulnerability.medusa, Url, Values, Token, proxies=proxies)
    Prompt("Spring")
