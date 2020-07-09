#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability
from Modules.Cms.ChanZhiEPS import ChanZhiEPSSQLInjectionVulnerability1
from Modules.Cms.ChanZhiEPS import ChanZhiEPSGetShellVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(ChanZhiEPSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(ChanZhiEPSSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(ChanZhiEPSGetShellVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ChanZhiEPS")