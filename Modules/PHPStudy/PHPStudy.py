#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.PHPStudy import PHPStudyBackdoor
from Modules.PHPStudy import PHPStudyPhpmyadminDefaultpwd
from Modules.PHPStudy import PHPStudyProbe
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(PHPStudyBackdoor.medusa, ** kwargs)
    Pool.Append(PHPStudyPhpmyadminDefaultpwd.medusa, ** kwargs)
    Pool.Append(PHPStudyProbe.medusa,** kwargs)
    Prompt("PHPStudy")