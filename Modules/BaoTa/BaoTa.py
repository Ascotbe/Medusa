#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.BaoTa import BtUnauthorizedAccessToPhpMyAdminDatabaseVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BtUnauthorizedAccessToPhpMyAdminDatabaseVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("BaoTa")



