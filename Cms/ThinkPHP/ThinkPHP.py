#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability
from Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability2
from Cms.ThinkPHP import ThinkPHPSqlInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(ThinkPHPSqlInjectionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("ThinkPHP")