#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("CMSMS")