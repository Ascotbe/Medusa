#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Nginx.NginxDirectoryTraversalVulnerability
import Nginx.NginxCRLFInjectionVulnerability
import time
def Main(url):
    try:
        vul=Nginx.NginxDirectoryTraversalVulnerability.NginxDirectoryTraversalVulnerability(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        vul=Nginx.NginxCRLFInjectionVulnerability.NginxCRLFInjectionVulnerability(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]NginxCRLFInjectionVulnerability Scan error")

