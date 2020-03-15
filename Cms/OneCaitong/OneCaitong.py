#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemSQLInjection
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemSQLInjection2
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles
from Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(OneCaitongElectronicProcurementSystemSQLInjection.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemSQLInjection2.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2.medusa, Url, Values, UnixTimestamp)
    Prompt("OneCaitong")
