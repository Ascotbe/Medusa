#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Tomcat import TomcatUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(TomcatUnauthorizedCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Tomcat")

