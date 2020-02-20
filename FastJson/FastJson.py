#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability2
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] FastJson component payload successfully loaded\033[0m")
    time.sleep(0.5)

