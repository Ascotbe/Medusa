#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Modules.Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ChanZhiEPSGetShellVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("ChanZhiEPS")