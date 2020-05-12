#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Rails import RubyOnRailsArbitraryFileReading
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(RubyOnRailsArbitraryFileReading.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Rails")


