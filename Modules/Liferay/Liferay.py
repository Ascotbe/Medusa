#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Liferay import LiferayPortalRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(LiferayPortalRemoteCommandExecutionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Liferay")