#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Emlog import EmlogSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EmlogSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Emlog")