#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Tomcat import TomcatUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,Proxies):
    ThreadPool.Append(TomcatUnauthorizedCommandExecutionVulnerability.medusa, Url, Values, Token,proxies=Proxies)
    Prompt("Tomcat")

