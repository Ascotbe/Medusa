#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CraftedWeb import CraftedWebCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CraftedWebCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CraftedWeb")