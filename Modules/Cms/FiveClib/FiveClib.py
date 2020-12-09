#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.FiveClib import FiveClibArbitraryFileDownloadVulnerability
from Modules.Cms.FiveClib import FiveClibArbitraryFileTraversalVulnerability
from Modules.Cms.FiveClib import FiveClibThereIsAnUnauthorizedLoophole
from Modules.Cms.FiveClib import FiveClibUnauthorizedAddAdministratorVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(FiveClibArbitraryFileDownloadVulnerability.medusa, **kwargs)
    Pool.Append(FiveClibArbitraryFileTraversalVulnerability.medusa, **kwargs)
    Pool.Append(FiveClibThereIsAnUnauthorizedLoophole.medusa, **kwargs)
    Pool.Append(FiveClibUnauthorizedAddAdministratorVulnerability.medusa, **kwargs)
    Prompt("FiveClib")