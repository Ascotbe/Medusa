#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability
from Modules.OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability
from Modules.OA.Tongda import TongdaOaUsesAnyAdministratorAccountToLogIn
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(TongdaOfficeAnywhereArbitraryFileUploadRemoteCommandExecutionVulnerability.medusa, Url, Values,
                      Token,proxies=proxies)
    ThreadPool.Append(TongdaOaUsesAnyAdministratorAccountToLogIn.medusa, Url, Values,Token,proxies=proxies)
    Prompt("Tongda")