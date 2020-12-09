#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Rails import RubyOnRailsArbitraryFileReading
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(RubyOnRailsArbitraryFileReading.medusa,** kwargs)
    Prompt("Rails")


