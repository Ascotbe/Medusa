#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability2
from Modules.OA.Ruvar import RuvarSystemSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(RuvarSystemSQLInjectionVulnerability.medusa, ** kwargs)
    Pool.Append(RuvarSystemSQLInjectionVulnerability2.medusa, ** kwargs)
    Pool.Append(RuvarSystemSQLInjectionVulnerability3.medusa,** kwargs)
    Prompt("Ruvar")
