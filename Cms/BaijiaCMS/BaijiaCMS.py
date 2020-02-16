#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BaijiaCMS import BaijiaCMSPathLeakVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BaijiaCMSPathLeakVulnerability.medusa, Url, Values, ProxyIp)
    print("BaijiaCMS component payload successfully loaded")