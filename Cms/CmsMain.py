#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Cms.SecCms import SecCms

def Main(Url,FileName,Values,ProxyIp):
    try:
        SecCms.Main(Url,FileName,Values,ProxyIp)
    except:
        pass