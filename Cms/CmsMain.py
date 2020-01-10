#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Cms.SecCms import SecCms
from Cms.Metinfo import Metinfo
from Cms.OneCaitong import OneCaitong
from Cms.Pboot import Pboot
from Cms.FiveClib import FiveClib
from Cms._74CMS import _74CMS
from Cms.Phpweb import Phpweb
def Main(Url,FileName,Values,ProxyIp):
    try:
        SecCms.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Metinfo.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        OneCaitong.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Pboot.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        FiveClib.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        _74CMS.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Phpweb.Main(Url,FileName,Values,ProxyIp)
    except:
        pass