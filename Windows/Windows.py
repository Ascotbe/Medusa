#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Windows import WindowsSMBv3ProtocolVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(WindowsSMBv3ProtocolVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Windows")
