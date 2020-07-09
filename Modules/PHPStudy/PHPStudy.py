#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.PHPStudy import PHPStudyBackdoor
from Modules.PHPStudy import PHPStudyPhpmyadminDefaultpwd
from Modules.PHPStudy import PHPStudyProbe
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(PHPStudyBackdoor.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(PHPStudyPhpmyadminDefaultpwd.medusa, Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(PHPStudyProbe.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("PHPStudy")