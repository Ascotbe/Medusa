#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Seeyou import Seeyou
from Modules.OA.Weaver import Weaver
from Modules.OA.Ruvar import Ruvar
from Modules.OA.Tongda import Tongda
def Main(ThreadPool,Url,Values,Token,proxies):
    Seeyou.Main(ThreadPool,Url,Values,Token,proxies)
    Weaver.Main(ThreadPool, Url, Values, Token,proxies)
    Ruvar.Main(ThreadPool, Url, Values, Token,proxies)
    Tongda.Main(ThreadPool, Url, Values, Token,proxies)