#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, **kwargs)
    Prompt("Harbor")