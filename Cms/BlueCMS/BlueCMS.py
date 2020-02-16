#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] BlueCMS component payload successfully loaded\033[0m")
    time.sleep(0.5)