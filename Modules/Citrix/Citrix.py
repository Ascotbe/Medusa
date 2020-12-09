#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Citrix import CitrixGatewayPathTraversalVulnerability
from Modules.Citrix import CitrixCertificationBypassesVulnerability
from Modules.Citrix import CitrixRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,**kwargs)
    Pool.Append(CitrixCertificationBypassesVulnerability.medusa, **kwargs)
    Pool.Append(CitrixGatewayPathTraversalVulnerability.medusa, **kwargs)
    Prompt("Citrix")



