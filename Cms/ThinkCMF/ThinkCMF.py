#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ThinkCMF import ThinkCMFArbitraryCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(ThinkCMFArbitraryCommandExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("ThinkCMF")

