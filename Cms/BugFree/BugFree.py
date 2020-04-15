#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BugFree import BugFreeFileContains
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BugFreeFileContains.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BugFree")