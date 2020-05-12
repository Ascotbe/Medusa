#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BEESCMS import BEESCMSLoginBypassVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BEESCMSLoginBypassVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BEESCMS")