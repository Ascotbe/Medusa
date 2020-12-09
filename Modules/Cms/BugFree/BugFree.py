#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BugFree import BugFreeFileContains
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(BugFreeFileContains.medusa, **kwargs)
    Prompt("BugFree")