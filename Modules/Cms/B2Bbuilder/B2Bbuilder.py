#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.B2Bbuilder import B2BbuilderBackgroundCommandExecutionVulnerability
from Modules.Cms.B2Bbuilder import B2BbuilderContainsVulnerabilitiesLocally
from Modules.Cms.B2Bbuilder import B2BbuilderHeadSQLInjectionVulnerability
from Modules.Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability
from Modules.Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability2
from Modules.Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability3
from Modules.Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability4
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(B2BbuilderBackgroundCommandExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderContainsVulnerabilitiesLocally.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderHeadSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability4.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("B2Bbuilder")