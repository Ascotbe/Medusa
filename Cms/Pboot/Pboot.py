#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Pboot import PbootCommandExecution
from Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PbootCommandExecution.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url, Values, ProxyIp)
    Prompt("Pboot")