#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Cyberwisdom")