#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability1
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability2
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability3
from Modules.Cms.Destoon import DestoonFrontDeskGetshellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(DestoonSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(DestoonSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(DestoonSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(DestoonFrontDeskGetshellVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Destoon")