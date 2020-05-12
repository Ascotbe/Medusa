#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.Phpweb import PhpwebArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(PhpwebArbitraryFileUploadVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("PHPweb")