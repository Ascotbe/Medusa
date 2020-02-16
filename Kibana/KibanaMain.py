#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Kibana import KibanaArbitraryFileReadVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(KibanaArbitraryFileReadVulnerability.medusa,Url,Values,ProxyIp)
    print("\033[1;40;32m[ + ] Kibana component payload successfully loaded\033[0m")
    time.sleep(0.5)