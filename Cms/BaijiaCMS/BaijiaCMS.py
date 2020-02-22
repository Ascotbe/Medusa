#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BaijiaCMS import BaijiaCMSPathLeakVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BaijiaCMSPathLeakVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("BaijiaCMS")