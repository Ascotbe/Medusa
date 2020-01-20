#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Cms.SecCms import SecCms
from Cms.Metinfo import Metinfo
from Cms.OneCaitong import OneCaitong
from Cms.Pboot import Pboot
from Cms.FiveClib import FiveClib
from Cms._74CMS import _74CMS
from Cms.Phpweb import Phpweb
from Cms.B2Bbuilder import B2Bbuilder
from Cms.BaijiaCMS import BaijiaCMS
from Cms.BearAdmin import BearAdmin
from Cms.BEESCMS import BEESCMS
from Cms.BlueCMS import BlueCMS
from Cms.Bocweb import Bocweb
from Cms.BugFree import BugFree
from Cms.BusBookingScript import BusBookingScript
from Cms.AbsolutEngine import AbsolutEngine
from Cms.AfterLogicWebMail import AfterLogicWebMail
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
    try:
        B2Bbuilder.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BaijiaCMS.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BusBookingScript.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BearAdmin.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BEESCMS.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BlueCMS.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        Bocweb.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        BugFree.Main(Url, FileName, Values, ProxyIp)
    except:
        pass
    try:
        AbsolutEngine.Main(Url, FileName, Values, ProxyIp)
    except:
        pass

    try:
        AfterLogicWebMail.Main(Url, FileName, Values, ProxyIp)
    except:
        pass

