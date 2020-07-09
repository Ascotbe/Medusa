#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Confluence import AtlassianConfluencePathTraversalAndCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(AtlassianConfluencePathTraversalAndCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Confluence")



