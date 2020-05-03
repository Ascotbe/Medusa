#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Modules.Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BlueCMS")