#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Metinfo import MetinfoArbitraryFileReadVulnerability
from Cms.Metinfo import MetinfoInformationDisclosureVulnerability
from Cms.Metinfo import MetinfoSQLInjectionVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(MetinfoArbitraryFileReadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(MetinfoInformationDisclosureVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(MetinfoSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Metinfo component payload successfully loaded\033[0m")
    time.sleep(0.5)
