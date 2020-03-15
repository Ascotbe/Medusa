#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Phpweb import PhpwebArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(PhpwebArbitraryFileUploadVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("PHPweb")