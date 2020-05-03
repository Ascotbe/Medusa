#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Pboot import PbootCommandExecution
from Modules.Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(PbootCommandExecution.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url, Values, Token,proxies=proxies)
    Prompt("Pboot")