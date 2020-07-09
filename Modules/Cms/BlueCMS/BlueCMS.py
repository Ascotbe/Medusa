#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Modules.Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BlueCMS")