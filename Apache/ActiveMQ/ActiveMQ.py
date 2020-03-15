#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.ActiveMQ import ActiveMQArbitraryFileWritingVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(ActiveMQArbitraryFileWritingVulnerability.medusa,Url,Values,UnixTimestamp)
    Prompt("ActiveMQ")
