#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BearAdmin import BearAdminArbitraryFileDownload
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BearAdminArbitraryFileDownload.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BearAdmin")