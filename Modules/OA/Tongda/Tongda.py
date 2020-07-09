#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability
from Modules.OA.Tongda import TongdaOaUsesAnyAdministratorAccountToLogIn
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(TongdaOaUsesAnyAdministratorAccountToLogIn.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Tongda")