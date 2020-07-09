#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Drupal import DrupalRemoteCodeExecutionVulnerability

from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(DrupalRemoteCodeExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Drupal")