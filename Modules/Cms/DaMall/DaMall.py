#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.DaMall import DaMallSystemSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(DaMallSystemSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("DaMall")