#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_45
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_54
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_55
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,Token,proxies):
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_45.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_54.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_55.medusa, Url, Values, Token,proxies=proxies)
    Prompt("SecCms")
