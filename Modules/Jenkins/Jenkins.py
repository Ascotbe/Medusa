#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Jenkins import JenkinsArbitraryFileReadVulnerability
from Modules.Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Modules.Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(JenkinsArbitraryFileReadVulnerability.medusa,    ** kwargs)
    Pool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, ** kwargs)
    Pool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, ** kwargs)
    Prompt("Jenkins")



