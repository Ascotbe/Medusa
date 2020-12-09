#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CTSCMS import CTSCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CTSCMSSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("CTSCMS")