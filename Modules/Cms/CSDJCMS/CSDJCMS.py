#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability
from Modules.Cms.CSDJCMS import CSDJCMSGetshell
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability1
from Modules.Cms.CSDJCMS import CSDJCMSSQLInjectionVulnerability2
from Modules.Cms.CSDJCMS import CSDJCMSGetshell1
from Modules.Cms.CSDJCMS import CSDJCMSStoredCrossSiteScriptingVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CSDJCMSSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(CSDJCMSGetshell.medusa, **kwargs)
    Pool.Append(CSDJCMSSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(CSDJCMSSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(CSDJCMSGetshell1.medusa, **kwargs)
    Pool.Append(CSDJCMSStoredCrossSiteScriptingVulnerability.medusa, **kwargs)
    Prompt("CSDJCMS")