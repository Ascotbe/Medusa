#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Tomcat import TomcatUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(TomcatUnauthorizedCommandExecutionVulnerability.medusa,**kwargs)
    Prompt("Tomcat")

