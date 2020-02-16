#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AfterLogicWebMailArbitraryFileContains.medusa, Url, Values, ProxyIp)
    print("AfterLogicWebMail component payload successfully loaded")