#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.EnableQ import EnableQSQLInjectionVulnerability
from Cms.EnableQ import EnableQSQLInjectionVulnerability1
from Cms.EnableQ import EnableQSQLInjectionVulnerability2
from Cms.EnableQ import EnableQArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(EnableQSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EnableQSQLInjectionVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EnableQSQLInjectionVulnerability2.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EnableQArbitraryFileUploadVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("EnableQ")