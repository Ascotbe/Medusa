#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Ecshop import EcoCMSSQLInjectionVulnerability
from Cms.Ecshop import EcoCMSSQLInjectionVulnerability1
from Cms.Ecshop import EcshopInformationLeakageVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EcoCMSSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcoCMSSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EcshopInformationLeakageVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Ecshop")