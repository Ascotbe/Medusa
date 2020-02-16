#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Nginx import NginxDirectoryTraversalVulnerability
from Nginx import NginxCRLFInjectionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(NginxDirectoryTraversalVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(NginxCRLFInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("Nginx component payload successfully loaded")


