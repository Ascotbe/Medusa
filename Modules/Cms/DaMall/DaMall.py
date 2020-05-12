#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.DaMall import DaMallSystemSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(DaMallSystemSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("DaMall")