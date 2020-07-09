#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Nginx import NginxDirectoryTraversalVulnerability
from Modules.Nginx import NginxCRLFInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(NginxDirectoryTraversalVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(NginxCRLFInjectionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Nginx")



