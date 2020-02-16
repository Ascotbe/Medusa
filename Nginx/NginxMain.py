#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Nginx import NginxDirectoryTraversalVulnerability
from Nginx import NginxCRLFInjectionVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(NginxDirectoryTraversalVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(NginxCRLFInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Nginx component payload successfully loaded\033[0m")
    time.sleep(0.5)



