#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability2
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability3
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability3.medusa,Url,Values,ProxyIp)
    print("\033[1;40;32m[ + ] Ruvar component payload successfully loaded\033[0m")
    time.sleep(0.5)
