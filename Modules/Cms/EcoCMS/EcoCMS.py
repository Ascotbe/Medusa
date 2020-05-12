#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EcoCMS import EcoCMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EcoCMSCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EcoCMS")