#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CTSCMS import CTSCMSSQLInjectionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CTSCMSSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("CTSCMS component payload successfully loaded")