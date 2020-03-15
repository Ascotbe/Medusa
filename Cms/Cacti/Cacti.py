#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Cacti import CactiSQLdatabasefileleakvulnerability,CactiSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CactiSQLdatabasefileleakvulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(CactiSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Cacti")