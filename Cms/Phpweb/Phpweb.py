#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Phpweb import PhpwebArbitraryFileUploadVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PhpwebArbitraryFileUploadVulnerability.medusa, Url, Values, ProxyIp)
    print("Phpweb component payload successfully loaded")