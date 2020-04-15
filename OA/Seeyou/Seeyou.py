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
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(SeeyouArbitraryFileReadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouMultipleSQLInjectionVulnerabilities.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouOALogInformationDisclosureVulnerability.medusa,Url,Values,Token,proxies=proxies)
    ThreadPool.Append(SeeyouSeeyouSystemFileArbitraryReadVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouSQLInjectionVulnerability3.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouStatusDefaultPwdVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouSystemFileArbitraryReadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouSystemFrameworkVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SeeyouSystemSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Seeyou")

