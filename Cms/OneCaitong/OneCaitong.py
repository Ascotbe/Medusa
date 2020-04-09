#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2.medusa, Url, Values, UnixTimestamp)
    Prompt("OneCaitong")
