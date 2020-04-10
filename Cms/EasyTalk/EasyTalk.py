#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability1
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability2
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability3
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability4
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability5
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability6
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability7
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability8
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability9
from Cms.EasyTalk import EasyTalkSQLInjectionVulnerability10
from Cms.EasyTalk import EasyTalkAnyFileInclusionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability3.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability4.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability5.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability6.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability7.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability8.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability9.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkSQLInjectionVulnerability10.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(EasyTalkAnyFileInclusionVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("EasyTalk")