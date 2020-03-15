#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Jenkins import JenkinsArbitraryFileReadVulnerability
from Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(JenkinsArbitraryFileReadVulnerability.medusa,Url,Values,UnixTimestamp)
    ThreadPool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Jenkins")



