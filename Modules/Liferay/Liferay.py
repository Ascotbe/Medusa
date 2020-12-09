#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Liferay import LiferayPortalRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(LiferayPortalRemoteCommandExecutionVulnerability.medusa,** kwargs)
    Prompt("Liferay")