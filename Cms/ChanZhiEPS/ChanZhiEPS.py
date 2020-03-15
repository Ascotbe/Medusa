#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(ChanZhiEPSGetShellVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("ChanZhiEPS")