#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability
from Cms.CSDJCMS import CSDJCMSGetshell
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability1
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability2
from Cms.CSDJCMS import CSDJCMSGetshell1
from Cms.CSDJCMS import CSDJCMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CSDJCMSGetshell.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CSDJCMSGetshell1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CSDJCMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CSDJCMS")