#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.FiveClib import FiveClibArbitraryFileDownloadVulnerability
from Cms.FiveClib import FiveClibArbitraryFileTraversalVulnerability
from Cms.FiveClib import FiveClibThereIsAnUnauthorizedLoophole
from Cms.FiveClib import FiveClibUnauthorizedAddAdministratorVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(FiveClibArbitraryFileDownloadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(FiveClibArbitraryFileTraversalVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(FiveClibThereIsAnUnauthorizedLoophole.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(FiveClibUnauthorizedAddAdministratorVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("FiveClib")