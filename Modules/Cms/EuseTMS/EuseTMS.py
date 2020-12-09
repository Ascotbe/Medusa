#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability1
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability2
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability3
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability4
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability5
from Modules.Cms.EuseTMS import EuseTMSSQLInjectionVulnerability6

from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EuseTMSSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability3.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability4.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability5.medusa, **kwargs)
    Pool.Append(EuseTMSSQLInjectionVulnerability6.medusa, **kwargs)

    Prompt("EuseTMS")