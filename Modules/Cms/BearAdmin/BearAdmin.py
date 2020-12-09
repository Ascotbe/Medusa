#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BearAdmin import BearAdminArbitraryFileDownload
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(BearAdminArbitraryFileDownload.medusa, **kwargs)
    Prompt("BearAdmin")