#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Destoon import DestoonSQLInjectionVulnerability1
from Cms.Destoon import DestoonSQLInjectionVulnerability2
from Cms.Destoon import DestoonSQLInjectionVulnerability3
from Cms.Destoon import DestoonFrontDeskGetshellVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(DestoonSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(DestoonSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(DestoonSQLInjectionVulnerability3.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(DestoonFrontDeskGetshellVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Destoon")