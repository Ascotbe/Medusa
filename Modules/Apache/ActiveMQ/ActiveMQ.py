#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.ActiveMQ import ActiveMQArbitraryFileWritingVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ActiveMQArbitraryFileWritingVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("ActiveMQ")
