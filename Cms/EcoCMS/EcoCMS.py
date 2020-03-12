#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.EcoCMS import EcoCMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(EcoCMSCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("EcoCMS")