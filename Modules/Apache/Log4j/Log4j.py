#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Log4j import Log4jRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(Log4jRemoteCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Log4j")