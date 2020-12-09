#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability
from Modules.Cms.CMSMS import CMSMSCrossSiteScriptingVulnerability1
from Modules.Cms.CMSMS import CMSMSReflectiveCrossSiteScriptingVulnerability
from Modules.Cms.CMSMS import CMSMSRemoteCodeExecutionVulnerability
from Modules.Cms.CMSMS import CMSMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(CMSMSCrossSiteScriptingVulnerability.medusa, **kwargs)
    Pool.Append(CMSMSCrossSiteScriptingVulnerability1.medusa, **kwargs)
    Pool.Append(CMSMSReflectiveCrossSiteScriptingVulnerability.medusa, **kwargs)
    Pool.Append(CMSMSRemoteCodeExecutionVulnerability.medusa, **kwargs)
    Pool.Append(CMSMSStoredCrossSiteScriptingVulnerability.medusa, **kwargs)
    Prompt("CMSMS")