#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Tomcat import TomcatUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt,Proxies

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(TomcatUnauthorizedCommandExecutionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Tomcat")

