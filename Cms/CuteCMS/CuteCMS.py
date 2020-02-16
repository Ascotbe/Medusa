#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CuteCMS import CuteCMSSQLinjection
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CuteCMSSQLinjection.medusa, Url, Values, ProxyIp)
    print("CuteCMS component payload successfully loaded")