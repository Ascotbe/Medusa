#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Citrix import CitrixGatewayPathTraversalVulnerability
from Modules.Citrix import CitrixCertificationBypassesVulnerability
from Modules.Citrix import CitrixRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CitrixCertificationBypassesVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    Pool.Append(CitrixGatewayPathTraversalVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Citrix")



