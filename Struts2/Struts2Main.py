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
import time

def Main(url):
    try:
        vul=Struts2.S2_001.S2_001(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-001 Scan error")
    try:
        vul =Struts2.S2_007.S2_007(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-007 Scan error")
    try:
        vul =Struts2.S2_012.S2_012(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-012 Scan error")
    try:
        vul =Struts2.S2_013.S2_013(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-013 Scan error")
    try:
        vul =Struts2.S2_016.S2_016(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-016 Scan error")
    try:
        vul =Struts2.S2_052.S2_052(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-052 Scan error")
    try:
        vul =Struts2.S2_053.S2_053(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-053 Scan error")
    try:
        vul =Struts2.S2_057.S2_057(url)
        filename = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        filenames = filename + ".txt"
        with open(filenames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul + "\n")
    except:
        print("[-]S2-057 Scan error")

