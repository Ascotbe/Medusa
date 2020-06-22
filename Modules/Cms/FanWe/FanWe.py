#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability1
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability2
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability3

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(FanWeSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(FanWeSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(FanWeSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(FanWeSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("FanWe")