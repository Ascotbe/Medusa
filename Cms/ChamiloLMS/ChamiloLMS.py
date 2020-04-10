#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ChamiloLMS import ChamiloLMSCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(ChamiloLMSCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("ChamiloLMS")