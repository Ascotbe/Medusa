#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Destoon import DestoonSQLInjectionVulnerability1
from Cms.Destoon import DestoonSQLInjectionVulnerability2
from Cms.Destoon import DestoonSQLInjectionVulnerability3
from Cms.Destoon import DestoonFrontDeskGetshellVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(DestoonSQLInjectionVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(DestoonSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(DestoonSQLInjectionVulnerability3.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(DestoonFrontDeskGetshellVulnerability.medusa, Url, Values, ProxyIp)
    print("Destoon component payload successfully loaded")