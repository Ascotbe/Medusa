#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("CMSMS")