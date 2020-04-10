#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Jenkins import JenkinsArbitraryFileReadVulnerability
from Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(JenkinsArbitraryFileReadVulnerability.medusa,Url,Values,Token,proxies=proxies)
    ThreadPool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Jenkins")



