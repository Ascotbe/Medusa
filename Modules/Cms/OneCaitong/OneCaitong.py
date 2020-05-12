#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles
from Modules.Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("OneCaitong")
