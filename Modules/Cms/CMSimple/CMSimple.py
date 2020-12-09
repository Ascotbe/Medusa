#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CMSimple import CMSimpleCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CMSimpleCrossSiteScriptingVulnerability.medusa, **kwargs)
    Prompt("CMSimple")