#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BearAdmin import BearAdminArbitraryFileDownload
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BearAdminArbitraryFileDownload.medusa, Url, Values, ProxyIp)
    print("BearAdmin component payload successfully loaded")