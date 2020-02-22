#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Mongo import MongoExpressRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(MongoExpressRemoteCodeExecutionVulnerability.medusa,Url,Values,ProxyIp)
    Prompt("Mongo")
