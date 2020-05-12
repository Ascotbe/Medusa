#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Mongo import MongoExpressRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(MongoExpressRemoteCodeExecutionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Mongo")
