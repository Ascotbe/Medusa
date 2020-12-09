#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability
from Modules.OA.Tongda import TongdaOaUsesAnyAdministratorAccountToLogIn
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability.medusa,** kwargs)
    Pool.Append(TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability.medusa, ** kwargs)
    Pool.Append(TongdaOaUsesAnyAdministratorAccountToLogIn.medusa, ** kwargs)
    Prompt("Tongda")