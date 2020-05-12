#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CsCMS import CsCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CsCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CsCMS")