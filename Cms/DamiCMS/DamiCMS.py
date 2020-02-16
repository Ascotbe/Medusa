#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability1
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability2
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability3
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability3.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] DamiCMS component payload successfully loaded\033[0m")
    time.sleep(0.5)