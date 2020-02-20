#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.ActiveMQ import ActiveMQArbitraryFileWritingVulnerability
import time

def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(ActiveMQArbitraryFileWritingVulnerability.medusa,Url,Values,ProxyIp)
    print("\033[1;40;32m[ + ] ActiveMQ component payload successfully loaded\033[0m")
    time.sleep(0.5)
