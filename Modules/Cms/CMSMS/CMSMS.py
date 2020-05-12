#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Modules.Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Modules.Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Modules.Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Modules.Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CMSMS")