#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EmpireCMS import EmpireCMSSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EmpireCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EmpireCMS")