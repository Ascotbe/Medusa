#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CactiSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Cacti")