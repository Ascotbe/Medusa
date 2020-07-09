#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.eYou import eYouSQLInjectionVulnerability
from Modules.Cms.eYou import eYouSQLInjectionVulnerability1
from Modules.Cms.eYou import eYouSQLInjectionVulnerability2
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(eYouSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(eYouSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(eYouSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("eYou")