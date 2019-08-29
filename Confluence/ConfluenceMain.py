#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Confluence.CVE_2019_3396
import time
import ClassCongregation
WriteFile=ClassCongregation.WriteFile#声明调用类集合中的WriteFile类

def Main(url,FileName):
    try:
        vul=Confluence.CVE_2019_3396.CVE_2019_3396(url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]CVE_2019_3396 Scan error")