#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url, Values, ProxyIp)
    print("BlueCMS component payload successfully loaded")