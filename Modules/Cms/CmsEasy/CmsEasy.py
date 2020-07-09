#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsEasy import CmsEasyCactiSQLInjectionVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability
from Modules.Cms.CmsEasy import CmsEasyCrossSiteScriptingVulnerability1
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CmsEasyCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CmsEasyCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CmsEasyCactiSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CmsEasy")