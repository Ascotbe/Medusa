#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability2
from OA.Ruvar import RuvarSystemSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(RuvarSystemSQLInjectionVulnerability3.medusa,Url,Values,ProxyIp)
    Prompt("Ruvar")
