#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CTSCMS import CTSCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CTSCMSSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("CTSCMS")