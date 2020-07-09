#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Coremail import CoremailConfigurationFileLeakVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CoremailConfigurationFileLeakVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Coremail")