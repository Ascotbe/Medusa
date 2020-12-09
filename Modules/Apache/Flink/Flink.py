#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Flink import FlinkUnauthorizedCommandExecutionVulnerability
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(FlinkUnauthorizedCommandExecutionVulnerability.medusa,**kwargs)
    Prompt("Flink")