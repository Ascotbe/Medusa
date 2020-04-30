#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Ecshop import EcshopSQLInjectionVulnerability
from Cms.Ecshop import EcshopSQLInjectionVulnerability1
from Cms.Ecshop import EcshopInformationLeakageVulnerability
from Cms.Ecshop import EcshopSQLInjectionVulnerability2
from Cms.Ecshop import EcshopRemoteCodeExecutionVulnerability
from Cms.Ecshop import EcshopSQLInjectionVulnerability3
from Cms.Ecshop import EcshopSQLInjectionVulnerability4
from Cms.Ecshop import EcshopSQLInjectionVulnerability5
from Cms.Ecshop import EcshopXssVulnerability


from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EcshopSQLInjectionVulnerability.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability1.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopInformationLeakageVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopRemoteCodeExecutionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability3.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability4.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability5.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopXssVulnerability.medusa, Url, Values, Token,proxies=proxies)

    Prompt("Ecshop")