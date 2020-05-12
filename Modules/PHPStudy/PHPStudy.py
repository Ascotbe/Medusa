#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.PHPStudy import PHPStudyBackdoor
from Modules.PHPStudy import PHPStudyPhpmyadminDefaultpwd
from Modules.PHPStudy import PHPStudyProbe
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(PHPStudyBackdoor.medusa, Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(PHPStudyPhpmyadminDefaultpwd.medusa, Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(PHPStudyProbe.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("PHPStudy")