#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Drupal import DrupalRemoteCodeExecutionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(DrupalRemoteCodeExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Drupal")