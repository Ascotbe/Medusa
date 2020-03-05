#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ChamiloLMS import ChamiloLMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(ChamiloLMSCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("ChamiloLMS")