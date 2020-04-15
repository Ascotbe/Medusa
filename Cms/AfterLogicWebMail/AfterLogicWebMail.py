#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(AfterLogicWebMailArbitraryFileContains.medusa, Url, Values, Token,proxies=proxies)
    Prompt("AfterLogicWebMail")