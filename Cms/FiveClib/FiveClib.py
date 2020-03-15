#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.FiveClib import FiveClibArbitraryFileDownloadVulnerability
from Cms.FiveClib import FiveClibArbitraryFileTraversalVulnerability
from Cms.FiveClib import FiveClibThereIsAnUnauthorizedLoophole
from Cms.FiveClib import FiveClibUnauthorizedAddAdministratorVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(FiveClibArbitraryFileDownloadVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(FiveClibArbitraryFileTraversalVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(FiveClibThereIsAnUnauthorizedLoophole.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(FiveClibUnauthorizedAddAdministratorVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("FiveClib")