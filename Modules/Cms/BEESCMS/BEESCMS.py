#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BEESCMS import BEESCMSLoginBypassVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(BEESCMSLoginBypassVulnerability.medusa, **kwargs)
    Prompt("BEESCMS")