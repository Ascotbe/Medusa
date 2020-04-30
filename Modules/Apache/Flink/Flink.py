#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Flink import FlinkUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,UnixTimestamp,proxies):
    ThreadPool.Append(FlinkUnauthorizedCommandExecutionVulnerability.medusa,Url,Values,UnixTimestamp,proxies=proxies)
    Prompt("Flink")