#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Emlog import EmlogSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(EmlogSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("Emlog")