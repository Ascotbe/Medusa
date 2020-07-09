#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Bocweb import BocwebNetworkSystemSensitiveInformationLeakage
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BocwebNetworkSystemSensitiveInformationLeakage.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Bocweb")