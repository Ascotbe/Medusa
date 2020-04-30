#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CmsEasy")