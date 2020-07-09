#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Cyberwisdom")