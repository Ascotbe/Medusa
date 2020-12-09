#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(AfterLogicWebMailArbitraryFileContains.medusa, **kwargs)
    Prompt("AfterLogicWebMail")