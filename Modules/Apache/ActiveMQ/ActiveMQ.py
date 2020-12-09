#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.ActiveMQ import ActiveMQArbitraryFileWritingVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(ActiveMQArbitraryFileWritingVulnerability.medusa,**kwargs)
    Prompt("ActiveMQ")
