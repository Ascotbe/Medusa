#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability2
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability3
from Modules.Cms.ThinkPHP import ThinkPHPSqlInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(ThinkPHPArbitraryCommandExecutionVulnerability.medusa, **kwargs)
    Pool.Append(ThinkPHPArbitraryCommandExecutionVulnerability2.medusa, **kwargs)
    Pool.Append(ThinkPHPArbitraryCommandExecutionVulnerability3.medusa, **kwargs)
    Pool.Append(ThinkPHPSqlInjectionVulnerability.medusa, **kwargs)
    Prompt("ThinkPHP")