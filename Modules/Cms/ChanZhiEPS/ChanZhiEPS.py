#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Modules.Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(ChanZhiEPSGetShellVulnerability.medusa, **kwargs)
    Prompt("ChanZhiEPS")