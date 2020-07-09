#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Dubbo import DubboProviderDefaultAntiSequenceVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(DubboProviderDefaultAntiSequenceVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Dubbo")



