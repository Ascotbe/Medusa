#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.FiveClib import FiveClibArbitraryFileDownloadVulnerability
from Modules.Cms.FiveClib import FiveClibArbitraryFileTraversalVulnerability
from Modules.Cms.FiveClib import FiveClibThereIsAnUnauthorizedLoophole
from Modules.Cms.FiveClib import FiveClibUnauthorizedAddAdministratorVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(FiveClibArbitraryFileDownloadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(FiveClibArbitraryFileTraversalVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(FiveClibThereIsAnUnauthorizedLoophole.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(FiveClibUnauthorizedAddAdministratorVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("FiveClib")