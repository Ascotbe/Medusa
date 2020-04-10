#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CraftedWeb import CraftedWebCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CraftedWebCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CraftedWeb")