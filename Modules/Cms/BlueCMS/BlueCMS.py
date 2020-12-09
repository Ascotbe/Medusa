#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BlueCMS import BlueCMSHasSQLinjectionVulnerability
from Modules.Cms.BlueCMS import BlueCMSMasterPasswordLoginVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(BlueCMSHasSQLinjectionVulnerability.medusa, **kwargs)
    Pool.Append(BlueCMSMasterPasswordLoginVulnerability.medusa, **kwargs)
    Prompt("BlueCMS")