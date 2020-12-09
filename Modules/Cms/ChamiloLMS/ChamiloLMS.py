#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ChamiloLMS import ChamiloLMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(ChamiloLMSCrossSiteScriptingVulnerability.medusa, **kwargs)
    Prompt("ChamiloLMS")