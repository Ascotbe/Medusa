#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability
from Cms.CSDJCMS import CSDJCMSGetshell
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability1
from Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability2
from Cms.CSDJCMS import CSDJCMSGetshell1
from Cms.CSDJCMS import CSDJCMSStoredCrossSiteScriptingVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CSDJCMSGetshell.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CSDJCMSSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CSDJCMSGetshell1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CSDJCMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] CSDJCMS component payload successfully loaded\033[0m")
    time.sleep(0.5)