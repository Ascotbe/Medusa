#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Cms.SecCms import SecCms
from Cms.Metinfo import Metinfo
def Main(Url,FileName,Values,ProxyIp):
    try:
        SecCms.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Metinfo.Main(Url,FileName,Values,ProxyIp)
    except:
        pass