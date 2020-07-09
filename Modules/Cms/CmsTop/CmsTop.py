#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CmsTop import CmsTopRemoteCodeExecution
from Modules.Cms.CmsTop import CmsTopSQLInjectionVulnerability
from Modules.Cms.CmsTop import CmsTopPathDisclosureVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(CmsTopRemoteCodeExecution.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CmsTopSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(CmsTopPathDisclosureVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("CmsTop")