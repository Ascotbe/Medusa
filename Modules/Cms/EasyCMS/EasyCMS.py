#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EasyCMSCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EasyCMSCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EasyCMS")