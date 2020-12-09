#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability1
from Modules.Cms.EnableQ import EnableQSQLInjectionVulnerability2
from Modules.Cms.EnableQ import EnableQArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EnableQSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(EnableQSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(EnableQSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(EnableQArbitraryFileUploadVulnerability.medusa, **kwargs)
    Prompt("EnableQ")