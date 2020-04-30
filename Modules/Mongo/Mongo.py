#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Mongo import MongoExpressRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(MongoExpressRemoteCodeExecutionVulnerability.medusa,Url,Values,Token,proxies=proxies)
    Prompt("Mongo")
