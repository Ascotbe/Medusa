#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability1
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability2
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability3
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability4
from Modules.Cms.Ecshop import EcshopCrossSiteScriptingVulnerability
from Modules.Cms.Ecshop import EcshopCrossSiteScriptingVulnerability1
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability5
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability6
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability7
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability8
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability9
from Modules.Cms.Ecshop import EcshopSQLInjectionVulnerability10

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(EcshopSQLInjectionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability4.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopCrossSiteScriptingVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopCrossSiteScriptingVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability5.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability6.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability7.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability8.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability9.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(EcshopSQLInjectionVulnerability10.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("Ecshop")