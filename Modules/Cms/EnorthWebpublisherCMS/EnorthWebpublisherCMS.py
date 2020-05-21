#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EnorthWebpublisherCMS import EnorthWebpublisherCMSSQLInjectionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EnorthWebpublisherCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EnorthWebpublisherCMS")