#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BearAdmin import BearAdminArbitraryFileDownload
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BearAdminArbitraryFileDownload.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BearAdmin")