#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BaijiaCMS import BaijiaCMSPathLeakVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BaijiaCMSPathLeakVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BaijiaCMS")