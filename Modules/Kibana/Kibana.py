#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Kibana import KibanaArbitraryFileReadVulnerability
from Modules.Kibana import KibanaRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(KibanaArbitraryFileReadVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(KibanaRemoteCommandExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Kibana")