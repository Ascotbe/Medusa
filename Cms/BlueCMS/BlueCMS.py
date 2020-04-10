#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("BlueCMS")