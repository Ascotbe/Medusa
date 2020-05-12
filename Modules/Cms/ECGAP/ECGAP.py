#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability1
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability2
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability3
from Modules.Cms.ECGAP import ECGAPSQLInjectionVulnerability4
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ECGAPSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability4.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ECGAP")