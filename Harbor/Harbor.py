#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Harbor import HarborAnyAdministratorRegistrationVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(HarborAnyAdministratorRegistrationVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Harbor component payload successfully loaded\033[0m")
    time.sleep(0.5)
