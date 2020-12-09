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

def Main(Pool,**kwargs):
    Pool.Append(B2BbuilderBackgroundCommandExecutionVulnerability.medusa, **kwargs)
    Pool.Append(B2BbuilderContainsVulnerabilitiesLocally.medusa, **kwargs)
    Pool.Append(B2BbuilderHeadSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability3.medusa, **kwargs)
    Pool.Append(B2BbuilderSQLInjectionVulnerability4.medusa, **kwargs)
    Prompt("B2Bbuilder")