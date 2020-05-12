#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Harbor")