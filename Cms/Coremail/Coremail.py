#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Coremail import CoremailConfigurationFileLeakVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CoremailConfigurationFileLeakVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Coremail")