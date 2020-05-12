#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Metinfo import MetinfoArbitraryFileReadVulnerability
from Modules.Cms.Metinfo import MetinfoInformationDisclosureVulnerability
from Modules.Cms.Metinfo import MetinfoSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(MetinfoArbitraryFileReadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(MetinfoInformationDisclosureVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(MetinfoSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Metinfo")