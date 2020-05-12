#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Confluence import AtlassianConfluencePathTraversalAndCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(AtlassianConfluencePathTraversalAndCommandExecutionVulnerability.medusa,Url,Values,proxies=proxies,**kwargs)
    Prompt("Confluence")



