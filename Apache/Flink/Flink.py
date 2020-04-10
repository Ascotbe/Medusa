#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Flink import FlinkUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt,Proxies

def Main(ThreadPool,Url,Values,UnixTimestamp,proxies_ip):
    proxies=Proxies().result(proxies_ip)
    ThreadPool.Append(FlinkUnauthorizedCommandExecutionVulnerability.medusa,Url,Values,UnixTimestamp,proxies=proxies)
    Prompt("Flink")