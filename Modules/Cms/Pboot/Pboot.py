#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Pboot import PbootCommandExecution
from Modules.Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(PbootCommandExecution.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Pboot")