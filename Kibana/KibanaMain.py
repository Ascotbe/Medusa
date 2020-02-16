#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Kibana import KibanaArbitraryFileReadVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(KibanaArbitraryFileReadVulnerability.medusa,Url,Values,ProxyIp)
    print("Kibana component payload successfully loaded")