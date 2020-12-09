#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Mongo import MongoExpressRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(MongoExpressRemoteCodeExecutionVulnerability.medusa,** kwargs)
    Prompt("Mongo")
