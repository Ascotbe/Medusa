#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BearAdmin import BearAdminArbitraryFileDownload
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BearAdminArbitraryFileDownload.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BearAdmin")