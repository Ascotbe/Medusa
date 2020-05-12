#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CmsEasy")