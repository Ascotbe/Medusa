#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Harbor")