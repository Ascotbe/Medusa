#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ThinkCMF import ThinkCMFArbitraryCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(ThinkCMFArbitraryCommandExecutionVulnerability.medusa, **kwargs)
    Prompt("ThinkCMF")

