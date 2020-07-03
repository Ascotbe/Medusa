#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Dubbo import DubboProviderDefaultAntiSequenceVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(DubboProviderDefaultAntiSequenceVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Dubbo")



