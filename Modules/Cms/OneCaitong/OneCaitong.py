#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles
from Modules.Cms.OneCaitong import OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles.medusa, **kwargs)
    Pool.Append(OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2.medusa, **kwargs)
    Prompt("OneCaitong")
