#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsTop import CmsTopRemoteCodeExecution
from Modules.Cms.CmsTop import CmsTopSQLInjectionVulnerability
from Modules.Cms.CmsTop import CmsTopPathDisclosureVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CmsTopRemoteCodeExecution.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CmsTopSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CmsTopPathDisclosureVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CmsTop")