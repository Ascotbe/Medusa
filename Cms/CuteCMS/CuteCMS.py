#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.CuteCMS import CuteCMSSQLinjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CuteCMSSQLinjection.medusa, Url, Values, UnixTimestamp)
    Prompt("CuteCMS")