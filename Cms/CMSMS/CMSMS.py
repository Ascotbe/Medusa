#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Cms.CMSMS import CMSMSDirectoryTraversalVulnerability
from Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability
import time

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(CMSMSDirectoryTraversalVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] CMSMS component payload successfully loaded\033[0m")
    time.sleep(0.5)