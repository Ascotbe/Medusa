#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import Struts2.S2_001
import Struts2.S2_007
import Struts2.S2_012
import Struts2.S2_013
import Struts2.S2_016
import Struts2.S2_052
import Struts2.S2_053
import Struts2.S2_057
import ClassCongregation


def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Struts2.S2_001.S2_001(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-001 Scan error")
    try:
        Medusa =Struts2.S2_007.S2_007(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-007 Scan error")
    try:
        Medusa =Struts2.S2_012.S2_012(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-012 Scan error")
    try:
        Medusa =Struts2.S2_013.S2_013(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-013 Scan error")
    try:
        Medusa =Struts2.S2_016.S2_016(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-016 Scan error")
    try:
        Medusa =Struts2.S2_052.S2_052(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-052 Scan error")
    try:
        Medusa =Struts2.S2_053.S2_053(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-053 Scan error")
    try:
        Medusa =Struts2.S2_057.S2_057(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]S2-057 Scan error")

