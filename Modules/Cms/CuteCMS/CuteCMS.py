#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CuteCMS import CuteCMSSQLinjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CuteCMSSQLinjection.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CuteCMS")