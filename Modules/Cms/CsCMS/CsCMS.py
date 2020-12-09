#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CsCMS import CsCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CsCMSSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("CsCMS")