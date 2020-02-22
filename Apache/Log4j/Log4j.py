#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Log4j import Log4jRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(Log4jRemoteCommandExecutionVulnerability.medusa,Url,Values,ProxyIp)
    Prompt("Log4j")