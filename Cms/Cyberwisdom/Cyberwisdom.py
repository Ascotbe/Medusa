#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url, Values, ProxyIp)
    print("Cyberwisdom component payload successfully loaded")