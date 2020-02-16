#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BusBookingScript import AdvancedBusBookingScriptSQLInjection
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AdvancedBusBookingScriptSQLInjection.medusa, Url, Values, ProxyIp)
    print("BusBookingScript component payload successfully loaded")