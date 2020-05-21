#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EmpireCMS import EmpireCMSSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EmpireCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EmpireCMS")