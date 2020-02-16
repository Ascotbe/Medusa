#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Spring import SpringReflectionFileDownloadVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SpringReflectionFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    print("Spring component payload successfully loaded")
