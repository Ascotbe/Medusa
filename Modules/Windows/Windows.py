#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Windows import WindowsSMBv3ProtocolVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(WindowsSMBv3ProtocolVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Windows")
