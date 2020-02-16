#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AbsolutEngine import AbsolutEngineXSS
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AbsolutEngineXSS.medusa, Url, Values, ProxyIp)
    print("AbsolutEngine component payload successfully loaded")