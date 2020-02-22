#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Phpweb import PhpwebArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(PhpwebArbitraryFileUploadVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("PHPweb")