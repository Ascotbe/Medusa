#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Modules.Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ChanZhiEPSGetShellVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ChanZhiEPS")