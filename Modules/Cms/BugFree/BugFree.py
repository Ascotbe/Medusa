#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BugFree import BugFreeFileContains
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BugFreeFileContains.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BugFree")