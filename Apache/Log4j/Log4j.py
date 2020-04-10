#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Log4j import Log4jRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt,Proxies

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(Log4jRemoteCommandExecutionVulnerability.medusa,Url,Values,Token,proxies=proxies)
    Prompt("Log4j")