#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EspCMS import EspCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EspCMSSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("EspCMS")