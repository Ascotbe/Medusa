#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EasyCMSCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyCMSCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EasyCMS")