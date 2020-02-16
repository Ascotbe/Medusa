#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import Seeyou
from OA.Weaver import Weaver
from OA.Ruvar import Ruvar
def Main(ThreadPool,Url,Values,ProxyIp):
    Seeyou.Main(ThreadPool,Url,Values,ProxyIp)
    Weaver.Main(ThreadPool, Url, Values, ProxyIp)
    Ruvar.Main(ThreadPool, Url, Values, ProxyIp)
