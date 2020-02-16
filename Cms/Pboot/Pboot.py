#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Pboot import PbootCommandExecution
from Cms.Pboot import PbootOnlineMessageDeskSqlInjection
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PbootCommandExecution.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PbootOnlineMessageDeskSqlInjection.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Pboot component payload successfully loaded\033[0m")
    time.sleep(0.5)
