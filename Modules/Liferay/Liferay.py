#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Liferay import LiferayPortalRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(LiferayPortalRemoteCommandExecutionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Liferay")