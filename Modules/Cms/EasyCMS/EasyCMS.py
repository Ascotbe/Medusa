#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability
from Modules.Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EasyCMSCrossSiteScriptingVulnerability.medusa, **kwargs)
    Pool.Append(EasyCMSCrossSiteScriptingVulnerability1.medusa, **kwargs)
    Prompt("EasyCMS")