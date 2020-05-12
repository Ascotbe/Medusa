#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Citrix import CitrixGatewayPathTraversalVulnerability
from Modules.Citrix import CitrixRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CitrixGatewayPathTraversalVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Citrix")



