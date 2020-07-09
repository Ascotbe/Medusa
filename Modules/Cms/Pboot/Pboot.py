#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Pboot import PbootCommandExecution
from Modules.Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(PbootCommandExecution.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Pboot")