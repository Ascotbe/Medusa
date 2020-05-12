#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability1
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability2
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("DamiCMS")