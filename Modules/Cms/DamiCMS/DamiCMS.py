#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability1
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability2
from Modules.Cms.DamiCMS import DamiCMSSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(DamiCMSSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(DamiCMSSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(DamiCMSSQLInjectionVulnerability3.medusa, **kwargs)
    Prompt("DamiCMS")