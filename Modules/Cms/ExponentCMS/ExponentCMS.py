#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ExponentCMS import ExponentCMSReflectiveXSSVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ExponentCMSReflectiveXSSVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ExponentCMS")