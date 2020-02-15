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
from Cms.CuteCMS import CuteCMS
from Cms.Cyberwisdom import Cyberwisdom
from Cms.CTSCMS import CTSCMS
from Cms.CMSMS import CMSMS
from Cms.Cacti import Cacti
from Cms.CSDJCMS import CSDJCMS
from Cms.Destoon import Destoon
from Cms.DamiCMS import DamiCMS
from Cms.DaMall import DaMall
import threading
def Main(Url,FileName,Values,ProxyIp):
    thread_lists=[]
    thread_lists.append(threading.Thread(target=SecCms.Main, args=(Url,FileName,Values,ProxyIp,)))
    thread_lists.append(threading.Thread(target=Metinfo.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=OneCaitong.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Pboot.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=FiveClib.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=_74CMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Phpweb.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=B2Bbuilder.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BaijiaCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BearAdmin.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BEESCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BlueCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Bocweb.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BugFree.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=BusBookingScript.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=AbsolutEngine.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=AfterLogicWebMail.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=CuteCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Cyberwisdom.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=CTSCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=CMSMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Cacti.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Destoon.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=DamiCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=DaMall.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=CSDJCMS.Main, args=(Url, FileName, Values, ProxyIp,)))
    for t in thread_lists:  # 开启列表中的多线程
        t.setDaemon(True)
        t.start()
        while True:
            # 判断正在运行的线程数量,如果小于5则退出while循环,
            # 进入for循环启动新的进程.否则就一直在while循环进入死循环
            if (len(threading.enumerate()) < 50):
                break
    for t in thread_lists:  # 除POC外功能总进度条
        t.join()
