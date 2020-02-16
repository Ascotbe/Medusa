#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BusBookingScript import AdvancedBusBookingScriptSQLInjection
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AdvancedBusBookingScriptSQLInjection.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] BusBookingScript component payload successfully loaded\033[0m")
    time.sleep(0.5)