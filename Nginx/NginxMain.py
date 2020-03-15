#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Nginx import NginxDirectoryTraversalVulnerability
from Nginx import NginxCRLFInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(NginxDirectoryTraversalVulnerability.medusa,Url,Values,UnixTimestamp)
    ThreadPool.Append(NginxCRLFInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Nginx")



