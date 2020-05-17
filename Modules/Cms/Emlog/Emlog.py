#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Emlog import EmlogSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EmlogSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Emlog")