#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ThinkCMF import ThinkCMFArbitraryCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ThinkCMFArbitraryCommandExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ThinkCMF")

