#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
import os
from ClassCongregation import UrlProcessing,AgentHeader
import requests
import threading
from tqdm import tqdm
class SensitiveData:
    def __init__(self):
        self.ThreadNumber=20000
        self.dirs= []#存放读取到的全部目录
        self.ExistenceDirectory=[]#存放存在的目录
        self.CopyDirectory=[]#存放多次迭代扫描的数据
        self.threa_list=[]#存放多线程
        self.Number=1
        global DirName
        if sys.platform == "win32" or sys.platform == "cygwin":
            DirName = os.path.split(os.path.realpath(__file__))[
                          0] + "\\Dir\\"
        elif sys.platform == "linux" or sys.platform == "darwin":
            DirName = os.path.split(os.path.realpath(__file__))[0] + "/Dir/"

        FileNames = os.listdir(DirName)
        for FileName in FileNames:
            if not os.path.isdir(FileName):  # 判断是不是文件夹
                with open(DirName + FileName, 'r', encoding='UTF-8') as f:
                    line = f.readline()
                    while line:
                        self.dirs.append(line.replace('\n', ''))  # 删除\n符号
                        line = f.readline()
    def WebDir(self,url):
        scheme, self.url, port = UrlProcessing().result(url)
        if port is None and scheme == 'https':
            port = 443
        elif port is None and scheme == 'http':
            port = 80
        else:
            port = port
        for dir in self.dirs:
            payload = scheme + "://" + self.url +":"+ str(port) +"/"+dir
            self.headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': AgentHeader().result("chrome"),
            }

            self.threa_list.append(threading.Thread(target=self.resp, args=(payload,self.headers,)))#调用自生的函数，以便开启多线程
        for t in tqdm(self.threa_list,ascii=True,desc="{}th iteration scan directory:".format(self.Number)):  # 开启列表中的多线程
            t.setDaemon(True)
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < self.ThreadNumber):
                    break
        for t in self.threa_list:
            t.join()
        self.Iterative()#调用一次迭代函数后他会自己继续迭代
    def Iterative(self):#迭代扫描
        if len(self.ExistenceDirectory)!=0:#判读是否有数据
            for data in self.ExistenceDirectory:
                self.write(data)#把存在的目录写入文件中
            self.CopyDirectory=self.ExistenceDirectory.copy()#把现存的数据拷贝到另一个列表中
            self.ExistenceDirectory.clear()#清空该列表
            self.threa_list.clear()#清空多线程池
            self.Number+=1
            for urls in self.CopyDirectory:
                for dir in self.dirs:
                    self.threa_list.append(threading.Thread(target=self.resp, args=(urls+"/"+dir, self.headers,)))
            for t in tqdm(self.threa_list,ascii=True,desc="{}th iteration scan directory:".format(self.Number)):  # 开启列表中的多线程
                t.setDaemon(True)
                t.start()
                while True:
                    # 判断正在运行的线程数量,如果小于5则退出while循环,
                    # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                    if (len(threading.enumerate()) < self.ThreadNumber):
                        break
            for t in self.threa_list:
                t.join()
            self.Iterative()#调用自身进行无线迭代
    def resp(self,payload,headers):
        try:
            resp = requests.head(payload, headers=headers, timeout=5, verify=False)
            if resp.status_code == 200 or resp.status_code ==302 or resp.status_code ==303 or resp.status_code ==307 or resp.status_code ==300 or resp.status_code ==203:
                self.ExistenceDirectory.append(payload)
        except:
            pass
    def write(self,data):
        global FileNames
        if sys.platform == "win32" or sys.platform == "cygwin":
            FileNames = os.path.split(os.path.realpath(__file__))[0]+"\\Target\\"+self.url + ".txt"#不需要输入后缀，只要名字就好
        elif sys.platform=="linux" or sys.platform=="darwin":
            FileNames = os.path.split(os.path.realpath(__file__))[0] + "/Target/" + self.url + ".txt"  # 不需要输入后缀，只要名字就好
        with open(FileNames, 'w+',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(data+"\n")



