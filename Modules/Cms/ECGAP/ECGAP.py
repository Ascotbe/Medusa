#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability1
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability2
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability3
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability4
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(ECGAPSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(ECGAPSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(ECGAPSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(ECGAPSQLInjectionVulnerability3.medusa, **kwargs)
    Pool.Append(ECGAPSQLInjectionVulnerability4.medusa, **kwargs)
    Prompt("ECGAP")