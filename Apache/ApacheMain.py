#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.ActiveMQ import ActiveMQArbitraryFileWritingVulnerability
from Apache.Log4j import Log4jRemoteCommandExecutionVulnerability


def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(ActiveMQArbitraryFileWritingVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(Log4jRemoteCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    print("Apache component payload successfully loaded")
