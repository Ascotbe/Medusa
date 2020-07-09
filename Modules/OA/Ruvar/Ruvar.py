#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability2
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(RuvarSystemSQLInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(RuvarSystemSQLInjectionVulnerability2.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(RuvarSystemSQLInjectionVulnerability3.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Ruvar")
