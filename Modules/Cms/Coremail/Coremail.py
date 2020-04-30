#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Coremail import CoremailConfigurationFileLeakVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CoremailConfigurationFileLeakVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Coremail")