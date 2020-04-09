#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Drupal import DrupalRemoteCodeExecutionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(DrupalRemoteCodeExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Drupal")