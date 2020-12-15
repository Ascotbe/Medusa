#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsTop import CmsTopSQLInjectionVulnerability
from Modules.Cms.CmsTop import CmsTopPathDisclosureVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CmsTopSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(CmsTopPathDisclosureVulnerability.medusa, **kwargs)
    Prompt("CmsTop")