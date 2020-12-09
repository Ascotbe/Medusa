#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.BaoTa import BtUnauthorizedAccessToPhpMyAdminDatabaseVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(BtUnauthorizedAccessToPhpMyAdminDatabaseVulnerability.medusa,**kwargs)
    Prompt("BaoTa")



