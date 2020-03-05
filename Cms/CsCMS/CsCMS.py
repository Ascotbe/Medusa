#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CsCMS import CsCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CsCMSSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("CsCMS")