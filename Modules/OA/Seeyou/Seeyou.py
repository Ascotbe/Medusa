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
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(SeeyouArbitraryFileReadVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouMultipleSQLInjectionVulnerabilities.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouOALogInformationDisclosureVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSeeyouSystemFileArbitraryReadVulnerability2.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSQLInjectionVulnerability2.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSQLInjectionVulnerability3.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouStatusDefaultPwdVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSystemFileArbitraryReadVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSystemFrameworkVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(SeeyouSystemSQLInjectionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Seeyou")

