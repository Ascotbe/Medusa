#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BEESCMS import BEESCMSLoginBypassVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BEESCMSLoginBypassVulnerability.medusa, Url, Values, ProxyIp)
    print("BEESCMS component payload successfully loaded")