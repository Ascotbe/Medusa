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
def Main(Pool,**kwargs):
    Pool.Append(SeeyouArbitraryFileReadVulnerability.medusa, ** kwargs)
    Pool.Append(SeeyouMultipleSQLInjectionVulnerabilities.medusa, ** kwargs)
    Pool.Append(SeeyouOALogInformationDisclosureVulnerability.medusa,** kwargs)
    Pool.Append(SeeyouSeeyouSystemFileArbitraryReadVulnerability2.medusa,** kwargs)
    Pool.Append(SeeyouSQLInjectionVulnerability2.medusa,** kwargs)
    Pool.Append(SeeyouSQLInjectionVulnerability3.medusa,** kwargs)
    Pool.Append(SeeyouStatusDefaultPwdVulnerability.medusa, ** kwargs)
    Pool.Append(SeeyouSystemFileArbitraryReadVulnerability.medusa,** kwargs)
    Pool.Append(SeeyouSystemFrameworkVulnerability.medusa, ** kwargs)
    Pool.Append(SeeyouSystemSQLInjectionVulnerability.medusa,** kwargs)
    Prompt("Seeyou")

