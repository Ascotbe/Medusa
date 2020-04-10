#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Phpweb import PhpwebArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(PhpwebArbitraryFileUploadVulnerability.medusa, Url, Values, Token,proxies=proxies)
    Prompt("PHPweb")