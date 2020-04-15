#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2.medusa, Url, Values, Token,proxies=proxies)
    Prompt("OneCaitong")
