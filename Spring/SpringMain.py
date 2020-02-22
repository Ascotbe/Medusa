#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Spring import SpringReflectionFileDownloadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SpringReflectionFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Spring")
