#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChamiloLMS import ChamiloLMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ChamiloLMSCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ChamiloLMS")