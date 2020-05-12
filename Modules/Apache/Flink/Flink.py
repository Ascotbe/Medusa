#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Flink import FlinkUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(FlinkUnauthorizedCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Flink")