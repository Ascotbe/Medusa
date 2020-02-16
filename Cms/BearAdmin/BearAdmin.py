#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BearAdmin import BearAdminArbitraryFileDownload
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BearAdminArbitraryFileDownload.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] BearAdmin component payload successfully loaded\033[0m")
    time.sleep(0.5)