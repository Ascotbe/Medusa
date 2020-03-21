#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Easethink import EasethinkSQLInjectionVulnerability
from Cms.Easethink import EasethinkSQLInjectionVulnerability1
from Cms.Easethink import EasethinkCookieInjectionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(EasethinkSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EasethinkSQLInjectionVulnerability1.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(EasethinkCookieInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Easethink")