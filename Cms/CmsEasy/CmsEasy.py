#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability
from Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("CmsEasy")