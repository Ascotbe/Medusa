#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BEESCMS import BEESCMSLoginBypassVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BEESCMSLoginBypassVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BEESCMS")