#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ECGAP import ECGAPSQLInjectionVulnerability
from Cms.ECGAP import ECGAPSQLInjectionVulnerability1
from Cms.ECGAP import ECGAPSQLInjectionVulnerability2
from Cms.ECGAP import ECGAPSQLInjectionVulnerability3
from Cms.ECGAP import ECGAPSQLInjectionVulnerability4
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(ECGAPSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability3.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(ECGAPSQLInjectionVulnerability4.medusa, Url, Values, Token,proxies=proxies)
    Prompt("ECGAP")