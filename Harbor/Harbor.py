#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Harbor import HarborAnyAdministratorRegistrationVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Harbor")