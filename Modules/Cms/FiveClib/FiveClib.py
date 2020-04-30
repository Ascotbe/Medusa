#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.FiveClib import FiveClibArbitraryFileDownloadVulnerability
from Modules.Cms.FiveClib import FiveClibArbitraryFileTraversalVulnerability
from Modules.Cms.FiveClib import FiveClibThereIsAnUnauthorizedLoophole
from Modules.Cms.FiveClib import FiveClibUnauthorizedAddAdministratorVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(FiveClibArbitraryFileDownloadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(FiveClibArbitraryFileTraversalVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(FiveClibThereIsAnUnauthorizedLoophole.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(FiveClibUnauthorizedAddAdministratorVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("FiveClib")