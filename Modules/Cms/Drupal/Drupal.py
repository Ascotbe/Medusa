#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Drupal import DrupalRemoteCodeExecutionVulnerability

from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(DrupalRemoteCodeExecutionVulnerability.medusa, **kwargs)
    Prompt("Drupal")