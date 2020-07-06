#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.BIG_IP import BIG_IPRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BIG_IPRemoteCodeExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("BIG-IP")



