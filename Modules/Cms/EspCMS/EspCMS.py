#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EspCMS import EspCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EspCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EspCMS")