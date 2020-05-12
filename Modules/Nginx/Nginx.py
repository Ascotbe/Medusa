#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Nginx import NginxDirectoryTraversalVulnerability
from Modules.Nginx import NginxCRLFInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(NginxDirectoryTraversalVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(NginxCRLFInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Nginx")



