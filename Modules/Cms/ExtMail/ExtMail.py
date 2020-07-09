#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ExtMail import ExtMailSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(ExtMailSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ExtMail")