#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EnorthWebpublisherCMS import EnorthWebpublisherCMSSQLInjectionVulnerability

from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EnorthWebpublisherCMSSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EnorthWebpublisherCMS")