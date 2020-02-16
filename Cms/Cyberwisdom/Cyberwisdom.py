#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Cyberwisdom component payload successfully loaded\033[0m")
    time.sleep(0.5)