#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Kibana import KibanaArbitraryFileReadVulnerability
from Modules.Kibana import KibanaRemoteCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(KibanaArbitraryFileReadVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(KibanaRemoteCommandExecutionVulnerability.medusa, Url, Values, proxies = proxies, ** kwargs)
    Prompt("Kibana")