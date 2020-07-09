#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from ClassCongregation import Prompt
from Modules.Struts2 import S2_001
from Modules.Struts2 import S2_005
from Modules.Struts2 import S2_008
from Modules.Struts2 import S2_009
from Modules.Struts2 import S2_015
from Modules.Struts2 import S2_016
from Modules.Struts2 import S2_045
#from Modules.Struts2 import S2_046
from Modules.Struts2 import S2_052
from Modules.Struts2 import S2_057


def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(S2_001.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_005.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_008.medusa, Url, Values, proxies=proxies, **kwargs)
    Pool.Append(S2_009.medusa, Url, Values, proxies=proxies, **kwargs)
    Pool.Append(S2_015.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_016.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_057.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_052.medusa, Url, Values, proxies = proxies, ** kwargs)
   # ThreadPool.Append(S2_046.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(S2_045.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Struts2")


