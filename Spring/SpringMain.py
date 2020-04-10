#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Spring import SpringReflectionFileDownloadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(SpringReflectionFileDownloadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Spring")
