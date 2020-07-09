#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Jenkins import JenkinsArbitraryFileReadVulnerability
from Modules.Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Modules.Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(JenkinsArbitraryFileReadVulnerability.medusa,    Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Jenkins")



