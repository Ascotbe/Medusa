#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Php import PhpStudyBackdoor
from Php import PhpstudyPhpmyadminDefaultpwd
from Php import PhpstudyProbe
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PhpStudyBackdoor.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PhpstudyPhpmyadminDefaultpwd.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PhpstudyProbe.medusa,Url,Values,ProxyIp)
    print("\033[1;40;32m[ + ] PHP component payload successfully loaded\033[0m")
    time.sleep(0.5)
