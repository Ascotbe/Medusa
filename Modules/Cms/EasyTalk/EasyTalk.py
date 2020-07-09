#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability1
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability2
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability3
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability4
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability5
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability6
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability7
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability8
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability9
from Modules.Cms.EasyTalk import EasyTalkSQLInjectionVulnerability10
from Modules.Cms.EasyTalk import EasyTalkAnyFileInclusionVulnerability

from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(EasyTalkSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability1.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability4.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability5.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability6.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability7.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability8.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability9.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkSQLInjectionVulnerability10.medusa, Url,Values,proxies=proxies,**kwargs)
    Pool.Append(EasyTalkAnyFileInclusionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("EasyTalk")