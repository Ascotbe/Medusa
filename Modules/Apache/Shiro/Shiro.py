#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Shiro import ShiroRememberMeDeserializationCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ShiroRememberMeDeserializationCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Shiro")

