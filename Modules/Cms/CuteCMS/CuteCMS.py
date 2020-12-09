#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.CuteCMS import CuteCMSSQLinjection
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(CuteCMSSQLinjection.medusa, **kwargs)
    Prompt("CuteCMS")