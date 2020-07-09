#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CMSimple import CMSimpleCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CMSimpleCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CMSimple")