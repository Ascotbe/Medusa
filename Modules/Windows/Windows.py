#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Windows import WindowsSMBv3ProtocolVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(WindowsSMBv3ProtocolVulnerability.medusa,  ** kwargs)
    Prompt("Windows")
