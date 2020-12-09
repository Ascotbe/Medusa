#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Easethink import EasethinkSQLInjectionVulnerability
from Modules.Cms.Easethink import EasethinkSQLInjectionVulnerability1
from Modules.Cms.Easethink import EasethinkCookieInjectionVulnerability
from Modules.Cms.Easethink import YiXiangSQLInjectionVulnerability
from Modules.Cms.Easethink import YiXiangSQLInjectionVulnerability1
from Modules.Cms.Easethink import YiXiangSQLInjectionVulnerability2
from Modules.Cms.Easethink import YiXiangSQLInjectionVulnerability3

from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(EasethinkSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(EasethinkSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(EasethinkCookieInjectionVulnerability.medusa, **kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability.medusa, **kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability1.medusa, **kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability2.medusa, **kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability3.medusa, **kwargs)
    Prompt("Easethink")