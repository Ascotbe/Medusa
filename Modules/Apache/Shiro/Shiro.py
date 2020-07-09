#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Shiro import ShiroRememberMeDeserializationCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(ShiroRememberMeDeserializationCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Shiro")

