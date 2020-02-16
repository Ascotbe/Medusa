#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CactiSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Cacti component payload successfully loaded\033[0m")
    time.sleep(0.5)