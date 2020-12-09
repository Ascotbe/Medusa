#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability1
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability2
from Modules.Cms.FanWe import FanWeSQLInjectionVulnerability3

from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(FanWeSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(FanWeSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(FanWeSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(FanWeSQLInjectionVulnerability3.medusa, **kwargs)
    Prompt("FanWe")