#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Kibana import KibanaArbitraryFileReadVulnerability
from Modules.Kibana import KibanaRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(KibanaArbitraryFileReadVulnerability.medusa,** kwargs)
    Pool.Append(KibanaRemoteCommandExecutionVulnerability.medusa, ** kwargs)
    Prompt("Kibana")