#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Modules.Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BlueCMS")