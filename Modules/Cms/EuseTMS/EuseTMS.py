#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability1
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability2
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability3
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability4
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability5
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability6

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability4.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability5.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EuseTMSSQLInjectionVulnerability6.medusa, Url,Values,proxies=proxies,**kwargs)

    Prompt("EuseTMS")