#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Citrix import CitrixGatewayPathTraversalVulnerability
from Citrix import CitrixRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CitrixRemoteCodeExecutionVulnerability.medusa,Url,Values,UnixTimestamp)
    ThreadPool.Append(CitrixGatewayPathTraversalVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Citrix")



