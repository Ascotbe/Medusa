#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Kibana import KibanaArbitraryFileReadVulnerability
from Kibana import KibanaRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(KibanaArbitraryFileReadVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(KibanaRemoteCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Kibana")