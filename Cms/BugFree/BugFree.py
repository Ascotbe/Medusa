#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BugFree import BugFreeFileContains
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BugFreeFileContains.medusa, Url, Values, ProxyIp)
    print("BugFree component payload successfully loaded")