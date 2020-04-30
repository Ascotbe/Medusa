#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Seeyou import SeeyouArbitraryFileReadVulnerability
from Modules.OA.Seeyou import SeeyouMultipleSQLInjectionVulnerabilities
from Modules.OA.Seeyou import SeeyouOALogInformationDisclosureVulnerability
from Modules.OA.Seeyou import SeeyouSeeyouSystemFileArbitraryReadVulnerability2
from Modules.OA.Seeyou import SeeyouSQLInjectionVulnerability2
from Modules.OA.Seeyou import SeeyouSQLInjectionVulnerability3
from Modules.OA.Seeyou import SeeyouStatusDefaultPwdVulnerability
from Modules.OA.Seeyou import SeeyouSystemFileArbitraryReadVulnerability
from Modules.OA.Seeyou import SeeyouSystemFrameworkVulnerability
from Modules.OA.Seeyou import SeeyouSystemSQLInjectionVulnerability
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

