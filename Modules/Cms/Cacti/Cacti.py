#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CactiSQLdatabasefileleakvulnerability.medusa, **kwargs)
    Pool.Append(CactiSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("Cacti")