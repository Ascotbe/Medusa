#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import time


class WriteFile:
    def __init__(self,FileName):
        if FileName == None:
            self.FileName = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        else:
            self.FileName = FileName


    def Write(self,Medusa):
        FileNames = self.FileName + ".txt"#不需要输入后缀，只要名字就好
        with open(FileNames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
               f.write(Medusa+ "\n")



class UserAgentS:
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


# a=UserAgentS("fireFox")
# b=a.UserAgent()
# print(b)
