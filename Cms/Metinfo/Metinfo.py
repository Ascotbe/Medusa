#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Metinfo import MetinfoArbitraryFileReadVulnerability
from Cms.Metinfo import MetinfoInformationDisclosureVulnerability
from Cms.Metinfo import MetinfoSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(MetinfoArbitraryFileReadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(MetinfoInformationDisclosureVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(MetinfoSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Metinfo")