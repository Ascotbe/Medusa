#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Metinfo import MetinfoArbitraryFileReadVulnerability
from Modules.Cms.Metinfo import MetinfoInformationDisclosureVulnerability
from Modules.Cms.Metinfo import MetinfoSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(MetinfoArbitraryFileReadVulnerability.medusa, **kwargs)
    Pool.Append(MetinfoInformationDisclosureVulnerability.medusa, **kwargs)
    Pool.Append(MetinfoSQLInjectionVulnerability.medusa, **kwargs)
    Prompt("Metinfo")