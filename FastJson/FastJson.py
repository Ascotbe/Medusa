#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    Prompt("FastJson")

