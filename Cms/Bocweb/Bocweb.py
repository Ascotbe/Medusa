#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Bocweb import BocwebNetworkSystemSensitiveInformationLeakage
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(BocwebNetworkSystemSensitiveInformationLeakage.medusa, Url, Values, UnixTimestamp)
    Prompt("Bocweb")