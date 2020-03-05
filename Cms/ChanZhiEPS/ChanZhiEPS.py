#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(ChanZhiEPSGetShellVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("ChanZhiEPS")