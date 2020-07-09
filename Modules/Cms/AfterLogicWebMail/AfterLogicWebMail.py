#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(AfterLogicWebMailArbitraryFileContains.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("AfterLogicWebMail")