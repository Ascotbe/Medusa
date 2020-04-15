#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Rails import RubyOnRailsArbitraryFileReading
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(RubyOnRailsArbitraryFileReading.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Rails")


