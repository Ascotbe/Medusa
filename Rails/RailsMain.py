#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Rails import RubyOnRailsArbitraryFileReading
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(RubyOnRailsArbitraryFileReading.medusa, Url, Values, ProxyIp)
    Prompt("Rails")


