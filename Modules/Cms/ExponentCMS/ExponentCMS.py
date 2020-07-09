#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ExponentCMS import ExponentCMSReflectiveXSSVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(ExponentCMSReflectiveXSSVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ExponentCMS")