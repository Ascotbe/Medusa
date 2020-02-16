#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Citrix import CitrixGatewayPathTraversalVulnerability
from Citrix import CitrixRemoteCodeExecutionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(CitrixGatewayPathTraversalVulnerability.medusa, Url, Values, ProxyIp)
    print("Citrix component payload successfully loaded")



