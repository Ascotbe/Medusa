#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability1
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability2
from Modules.Cms.Destoon import DestoonSQLInjectionVulnerability3
from Modules.Cms.Destoon import DestoonFrontDeskGetshellVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(DestoonSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(DestoonSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(DestoonSQLInjectionVulnerability3.medusa, **kwargs)
    Pool.Append(DestoonFrontDeskGetshellVulnerability.medusa, **kwargs)
    Prompt("Destoon")