#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Ecshop import EcshopSQLInjectionVulnerability
from Cms.Ecshop import EcshopSQLInjectionVulnerability1
from Cms.Ecshop import EcshopInformationLeakageVulnerability
from Cms.Ecshop import EcshopSQLInjectionVulnerability2
from Cms.Ecshop import EcshopRemoteCodeExecutionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EcshopSQLInjectionVulnerability.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability1.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopInformationLeakageVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Ecshop")