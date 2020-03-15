#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability
from Cms.Cyberwisdom import CyberwisdomArbitraryFileDownloadVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CyberwisdomArbitraryFileDownloadVulnerability2.medusa, Url, Values, UnixTimestamp)
    Prompt("Cyberwisdom")