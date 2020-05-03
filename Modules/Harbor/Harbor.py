#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Harbor")