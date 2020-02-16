#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Citrix import CitrixGatewayPathTraversalVulnerability
from Citrix import CitrixRemoteCodeExecutionVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(CitrixGatewayPathTraversalVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Citrix component payload successfully loaded\033[0m")
    time.sleep(0.5)



