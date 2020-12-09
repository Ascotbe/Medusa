#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Coremail import CoremailConfigurationFileLeakVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CoremailConfigurationFileLeakVulnerability.medusa, **kwargs)
    Prompt("Coremail")