#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Struts2 import S2_001
from Struts2 import S2_007
from Struts2 import S2_012
from Struts2 import S2_013
from Struts2 import S2_016
from Struts2 import S2_052
from Struts2 import S2_053
from Struts2 import S2_057
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(S2_001.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_007.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_012.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_013.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_016.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_052.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_053.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(S2_057.medusa, Url, Values, ProxyIp)
    print("Struts2 component payload successfully loaded")

