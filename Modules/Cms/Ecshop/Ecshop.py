#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability1
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability2
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability3
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability4
from Modules.Cms.Ecshop import EcshopCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EcshopSQLInjectionVulnerability.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability1.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability2.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability3.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopSQLInjectionVulnerability4.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(EcshopCrossSiteScriptingVulnerability.medusa, Url, Values, Token, proxies=proxies)
    Prompt("Ecshop")