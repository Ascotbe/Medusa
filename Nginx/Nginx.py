#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Nginx.NginxDirectoryTraversalVulnerability
import Nginx.NginxCRLFInjectionVulnerability
import time
import ClassCongregation
WriteFile=ClassCongregation.WriteFile#声明调用类集合中的WriteFile类
def Main(url,FileName):
    try:
        vul=Nginx.NginxDirectoryTraversalVulnerability.NginxDirectoryTraversalVulnerability(url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        vul=Nginx.NginxCRLFInjectionVulnerability.NginxCRLFInjectionVulnerability(url)
        WriteFile.Write(vul, FileName)
    except:
        print("[-]NginxCRLFInjectionVulnerability Scan error")

