#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Bocweb import BocwebNetworkSystemSensitiveInformationLeakage
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BocwebNetworkSystemSensitiveInformationLeakage.medusa, Url, Values, ProxyIp)
    print("Bocweb component payload successfully loaded")