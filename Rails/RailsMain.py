#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Rails import RubyOnRailsArbitraryFileReading
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(RubyOnRailsArbitraryFileReading.medusa, Url, Values, ProxyIp)
    print("Rails component payload successfully loaded")


