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
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EasethinkSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasethinkSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasethinkCookieInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(YiXiangSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Easethink")