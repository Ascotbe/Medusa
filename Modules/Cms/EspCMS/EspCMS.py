#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EspCMS import EspCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EspCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EspCMS")