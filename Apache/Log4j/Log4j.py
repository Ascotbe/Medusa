#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Log4j import Log4jRemoteCommandExecutionVulnerability
import time

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(Log4jRemoteCommandExecutionVulnerability.medusa,Url,Values,ProxyIp)
    print("\033[1;40;32m[ + ] Log4j component payload successfully loaded\033[0m")
    time.sleep(0.5)