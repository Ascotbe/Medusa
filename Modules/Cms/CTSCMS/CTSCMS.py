#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CTSCMS import CTSCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CTSCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CTSCMS")