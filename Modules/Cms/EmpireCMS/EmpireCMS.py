#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EmpireCMS import EmpireCMSSQLInjectionVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(EmpireCMSSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("EmpireCMS")