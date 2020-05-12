#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Windows import WindowsSMBv3ProtocolVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(WindowsSMBv3ProtocolVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Windows")
