#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Confluence import AtlassianConfluencePathTraversalAndCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(AtlassianConfluencePathTraversalAndCommandExecutionVulnerability.medusa,**kwargs)
    Prompt("Confluence")



