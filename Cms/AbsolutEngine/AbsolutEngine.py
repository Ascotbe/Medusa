#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AbsolutEngine import AbsolutEngineXSS
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AbsolutEngineXSS.medusa, Url, Values, ProxyIp)
    Prompt("AbsolutEngine")