#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CactiSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Cacti")