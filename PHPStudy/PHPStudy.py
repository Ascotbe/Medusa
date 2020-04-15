#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from PHPStudy import PHPStudyBackdoor
from PHPStudy import PHPStudyPhpmyadminDefaultpwd
from PHPStudy import PHPStudyProbe
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(PHPStudyBackdoor.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(PHPStudyPhpmyadminDefaultpwd.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(PHPStudyProbe.medusa,Url,Values,Token,proxies=proxies)
    Prompt("PHPStudy")