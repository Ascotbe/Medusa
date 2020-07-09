#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ThinkCMF import ThinkCMFArbitraryCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(ThinkCMFArbitraryCommandExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ThinkCMF")

