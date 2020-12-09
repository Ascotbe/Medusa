#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.eYou import eYouSQLInjectionVulnerability
from Modules.Cms.eYou import eYouSQLInjectionVulnerability1
from Modules.Cms.eYou import eYouSQLInjectionVulnerability2
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(eYouSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(eYouSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(eYouSQLInjectionVulnerability2.medusa, **kwargs)
    Prompt("eYou")