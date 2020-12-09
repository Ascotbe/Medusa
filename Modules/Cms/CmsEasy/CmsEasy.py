#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, **kwargs)
    Pool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, **kwargs)
    Pool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("CmsEasy")