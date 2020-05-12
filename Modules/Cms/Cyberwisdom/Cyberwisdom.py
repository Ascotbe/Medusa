#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Cyberwisdom")