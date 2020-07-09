#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability1
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability2
from Modules.Cms.EnableQ import EnableQArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EnableQSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EnableQSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EnableQSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EnableQArbitraryFileUploadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EnableQ")