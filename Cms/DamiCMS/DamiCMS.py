#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability1
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability2
from Cms.DamiCMS import DamiCMSSQLInjectionVulnerability3
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability2.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(DamiCMSSQLInjectionVulnerability3.medusa, Url, Values, UnixTimestamp)
    Prompt("DamiCMS")