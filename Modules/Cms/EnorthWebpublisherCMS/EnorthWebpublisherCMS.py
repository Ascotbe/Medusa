#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EnorthWebpublisherCMS import EnorthWebpublisherCMSSQLInjectionVulnerability

from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EnorthWebpublisherCMSSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("EnorthWebpublisherCMS")