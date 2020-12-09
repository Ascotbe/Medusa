#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Bocweb import BocwebNetworkSystemSensitiveInformationLeakage
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(BocwebNetworkSystemSensitiveInformationLeakage.medusa, **kwargs)
    Prompt("Bocweb")