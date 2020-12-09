#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Dubbo import DubboProviderDefaultAntiSequenceVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(DubboProviderDefaultAntiSequenceVulnerability.medusa,**kwargs)
    Prompt("Dubbo")



