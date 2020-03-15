#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Pboot import PbootCommandExecution
from Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(PbootCommandExecution.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url, Values, UnixTimestamp)
    Prompt("Pboot")