#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CmsTop import CmsTopRemoteCodeExecution
from Cms.CmsTop import CmsTopSQLInjectionVulnerability
from Cms.CmsTop import CmsTopPathDisclosureVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CmsTopRemoteCodeExecution.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CmsTopSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CmsTopPathDisclosureVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] CmsTop component payload successfully loaded\033[0m")
    time.sleep(0.5)