#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Harbor")