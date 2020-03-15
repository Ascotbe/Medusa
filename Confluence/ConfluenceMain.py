#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Confluence import AtlassianConfluencePathTraversalAndCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(AtlassianConfluencePathTraversalAndCommandExecutionVulnerability.medusa,Url,Values,UnixTimestamp)
    Prompt("Confluence")



