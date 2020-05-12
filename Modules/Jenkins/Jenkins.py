#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Jenkins import JenkinsArbitraryFileReadVulnerability
from Modules.Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Modules.Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(JenkinsArbitraryFileReadVulnerability.medusa,    Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Jenkins")



