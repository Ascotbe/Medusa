#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BearAdmin import BearAdminArbitraryFileDownload
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(BearAdminArbitraryFileDownload.medusa, Url, Values, UnixTimestamp)
    Prompt("BearAdmin")