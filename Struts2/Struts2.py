#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from ClassCongregation import Prompt
from Struts2 import S2_001
from Struts2 import S2_007
from Struts2 import S2_012
from Struts2 import S2_013
from Struts2 import S2_016
from Struts2 import S2_052
from Struts2 import S2_053
from Struts2 import S2_005
from Struts2 import S2_008_1
from Struts2 import S2_008_2
from Struts2 import S2_009
from Struts2 import S2_019
from Struts2 import S2_020
from Struts2 import S2_032
from Struts2 import S2_033
from Struts2 import S2_037
from Struts2 import S2_045
from Struts2 import S2_046
from Struts2 import S2_048
from Struts2 import S2_057
from Struts2 import S2_Devmode

def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(S2_001.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_007.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_012.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_013.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_016.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_052.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_053.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_005.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_008_1.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_008_2.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_009.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_019.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_020.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_032.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_033.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_037.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_057.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_046.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_048.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_045.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(S2_Devmode.medusa, Url, Values, Token,proxies=proxies)

    Prompt("Struts2")


