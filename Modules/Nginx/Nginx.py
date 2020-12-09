#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Nginx import NginxDirectoryTraversalVulnerability
from Modules.Nginx import NginxCRLFInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(NginxDirectoryTraversalVulnerability.medusa,** kwargs)
    Pool.Append(NginxCRLFInjectionVulnerability.medusa, ** kwargs)
    Prompt("Nginx")



