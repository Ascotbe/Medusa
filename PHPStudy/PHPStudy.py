#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from PHPStudy import PHPStudyBackdoor
from PHPStudy import PHPStudyPhpmyadminDefaultpwd
from PHPStudy import PHPStudyProbe
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(PHPStudyBackdoor.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(PHPStudyPhpmyadminDefaultpwd.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(PHPStudyProbe.medusa,Url,Values,UnixTimestamp)
    Prompt("PHPStudy")