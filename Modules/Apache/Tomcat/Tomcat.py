#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Tomcat import TomcatUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(TomcatUnauthorizedCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Tomcat")

