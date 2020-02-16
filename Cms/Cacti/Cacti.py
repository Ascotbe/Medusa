#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CactiSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("Cacti component payload successfully loaded")