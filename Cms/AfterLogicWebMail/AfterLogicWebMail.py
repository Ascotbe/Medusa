#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(AfterLogicWebMailArbitraryFileContains.medusa, Url, Values, UnixTimestamp)
    Prompt("AfterLogicWebMail")