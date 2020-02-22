#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("BlueCMS")