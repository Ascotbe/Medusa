#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability
from Modules.Cms.CSDJCMS import CSDJCMSGetshell
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability1
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability2
from Modules.Cms.CSDJCMS import CSDJCMSGetshell1
from Modules.Cms.CSDJCMS import CSDJCMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CSDJCMSGetshell.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CSDJCMSGetshell1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CSDJCMSStoredCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CSDJCMS")