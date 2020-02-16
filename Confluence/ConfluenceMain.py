#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Confluence import AtlassianConfluencePathTraversalAndCommandExecutionVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AtlassianConfluencePathTraversalAndCommandExecutionVulnerability.medusa,Url,Values,ProxyIp)
    print("Citrix component payload successfully loaded")




