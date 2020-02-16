#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Cms.CMSMS import CMSMSDirectoryTraversalVulnerability
from Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CMSMSDirectoryTraversalVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    print("CMSMS component payload successfully loaded")