#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Cms.Kxmail.Kxmail_login_server_sqli
import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Cms.Kxmail.Kxmail_login_server_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
