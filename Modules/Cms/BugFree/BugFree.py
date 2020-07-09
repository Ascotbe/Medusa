#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BugFree import BugFreeFileContains
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BugFreeFileContains.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BugFree")