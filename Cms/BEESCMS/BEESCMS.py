#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BEESCMS import BEESCMSLoginBypassVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BEESCMSLoginBypassVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BEESCMS")