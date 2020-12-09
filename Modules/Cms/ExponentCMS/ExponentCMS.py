#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ExponentCMS import ExponentCMSReflectiveXSSVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(ExponentCMSReflectiveXSSVulnerability.medusa, **kwargs)
    Prompt("ExponentCMS")