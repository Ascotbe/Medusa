#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Flink import FlinkUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(FlinkUnauthorizedCommandExecutionVulnerability.medusa,Url,Values,ProxyIp)
    Prompt("Flink")