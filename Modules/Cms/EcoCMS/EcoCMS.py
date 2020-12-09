#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EcoCMS import EcoCMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EcoCMSCrossSiteScriptingVulnerability.medusa, **kwargs)
    Prompt("EcoCMS")