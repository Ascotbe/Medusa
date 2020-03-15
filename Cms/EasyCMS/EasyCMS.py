#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability
from Cms.EasyCMS import EasyCMSCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(EasyCMSCrossSiteScriptingVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EasyCMSCrossSiteScriptingVulnerability1.medusa, Url, Values, UnixTimestamp)
    Prompt("EasyCMS")