#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CactiSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Cacti")