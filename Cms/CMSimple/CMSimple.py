#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSimple import CMSimpleCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CMSimpleCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CMSimple")