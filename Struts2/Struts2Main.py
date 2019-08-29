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
WriteFile=ClassCongregation.WriteFile#声明调用类集合中的WriteFile类

def Main(Url,FileName):
    try:
        vul=Struts2.S2_001.S2_001(Url)
        WriteFile.Write(vul,FileName)
    except:
        print("[-]S2-001 Scan error")
    try:
        vul =Struts2.S2_007.S2_007(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-007 Scan error")
    try:
        vul =Struts2.S2_012.S2_012(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-012 Scan error")
    try:
        vul =Struts2.S2_013.S2_013(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-013 Scan error")
    try:
        vul =Struts2.S2_016.S2_016(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-016 Scan error")
    try:
        vul =Struts2.S2_052.S2_052(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-052 Scan error")
    try:
        vul =Struts2.S2_053.S2_053(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-053 Scan error")
    try:
        vul =Struts2.S2_057.S2_057(Url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]S2-057 Scan error")

