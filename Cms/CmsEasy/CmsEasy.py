#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability,CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("CmsEasy")