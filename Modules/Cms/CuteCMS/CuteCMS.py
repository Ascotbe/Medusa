#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CuteCMS import CuteCMSSQLinjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CuteCMSSQLinjection.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CuteCMS")