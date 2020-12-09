#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Pboot import PbootCommandExecution
from Modules.Cms.Pboot import PbootOnlineMessageDeskSqlInjection
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(PbootCommandExecution.medusa, **kwargs)
    Pool.Append(PbootOnlineMessageDeskSqlInjection.medusa, **kwargs)
    Prompt("Pboot")