#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.EnableQ import EnableQSQLInjectionVulnerability
from Cms.EnableQ import EnableQSQLInjectionVulnerability1
from Cms.EnableQ import EnableQSQLInjectionVulnerability2
from Cms.EnableQ import EnableQArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EnableQSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EnableQSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EnableQSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EnableQArbitraryFileUploadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("EnableQ")