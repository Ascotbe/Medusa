#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.OA.Seeyou import Seeyou
from Modules.OA.Weaver import Weaver
from Modules.OA.Ruvar import Ruvar
from Modules.OA.Tongda import Tongda
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    Seeyou.Main(ThreadPool,Url, Values, proxies, ** kwargs)
    Weaver.Main(ThreadPool,Url, Values, proxies, ** kwargs)
    Ruvar.Main(ThreadPool,Url, Values, proxies, ** kwargs)
    Tongda.Main(ThreadPool, Url, Values,proxies, ** kwargs)