#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.DaMall import DaMallSystemSQLInjectionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(DaMallSystemSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("DaMall component payload successfully loaded")