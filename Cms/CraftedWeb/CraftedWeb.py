#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CraftedWeb import CraftedWebCrossSiteScriptingVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CraftedWebCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    print("CraftedWeb component payload successfully loaded")