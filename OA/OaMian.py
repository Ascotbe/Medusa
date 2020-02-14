#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import Seeyou
from OA.Weaver import Weaver
from OA.Ruvar import Ruvar
import threading
def Main(Url,FileName,Values,ProxyIp):
    thread_lists = []
    thread_lists.append(threading.Thread(target=Seeyou.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Weaver.Main, args=(Url, FileName, Values, ProxyIp,)))
    thread_lists.append(threading.Thread(target=Ruvar.Main, args=(Url, FileName, Values, ProxyIp,)))
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