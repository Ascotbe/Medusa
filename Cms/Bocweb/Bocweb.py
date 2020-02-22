#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Bocweb import BocwebNetworkSystemSensitiveInformationLeakage
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BocwebNetworkSystemSensitiveInformationLeakage.medusa, Url, Values, ProxyIp)
    Prompt("Bocweb")