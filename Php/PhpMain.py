#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Php import PhpStudyBackdoor
from Php import PhpstudyPhpmyadminDefaultpwd
from Php import PhpstudyProbe
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PhpStudyBackdoor.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PhpstudyPhpmyadminDefaultpwd.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(PhpstudyProbe.medusa,Url,Values,ProxyIp)
    Prompt("PHPStudy")