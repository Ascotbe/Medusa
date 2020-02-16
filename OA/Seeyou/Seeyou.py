#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import SeeyouArbitraryFileReadVulnerability
from OA.Seeyou import SeeyouMultipleSQLInjectionVulnerabilities
from OA.Seeyou import SeeyouOALogInformationDisclosureVulnerability
from OA.Seeyou import SeeyouSeeyouSystemFileArbitraryReadVulnerability2
from OA.Seeyou import SeeyouSQLInjectionVulnerability2
from OA.Seeyou import SeeyouSQLInjectionVulnerability3
from OA.Seeyou import SeeyouStatusDefaultPwdVulnerability
from OA.Seeyou import SeeyouSystemFileArbitraryReadVulnerability
from OA.Seeyou import SeeyouSystemFrameworkVulnerability
from OA.Seeyou import SeeyouSystemSQLInjectionVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SeeyouArbitraryFileReadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouMultipleSQLInjectionVulnerabilities.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouOALogInformationDisclosureVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(SeeyouSeeyouSystemFileArbitraryReadVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouSQLInjectionVulnerability3.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouStatusDefaultPwdVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouSystemFileArbitraryReadVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouSystemFrameworkVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SeeyouSystemSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Seeyou component payload successfully loaded\033[0m")
    time.sleep(0.5)

