#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Modules.Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, **kwargs)
    Pool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, **kwargs)
    Prompt("Cyberwisdom")