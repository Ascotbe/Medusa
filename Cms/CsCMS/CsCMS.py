#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CsCMS import CsCMSSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CsCMSSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CsCMS")