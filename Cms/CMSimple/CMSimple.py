#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSimple import CMSimpleCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CMSimpleCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("CMSimple")