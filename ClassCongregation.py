#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import urllib.parse
import nmap
import requests
import pymysql
import sqlite3
from scrapy.selector import Selector
from tqdm import tqdm
import logging
import os
import re
import json
import random
import sys
import time
import threading
def IpProcess(Url):
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)
LoopholesList=[]#漏洞个数列表
def NumberOfLoopholes():#漏洞个数输出函数
    print("\033[1;40;32m[ ! ] The number of vulnerabilities scanned was:\033[0m"+"\033[1;40;36m {}             \033[0m".format(len(LoopholesList)))

class WriteFile:#写入文件类
    def result(self,TargetName,Medusa):
        self.FileName=TargetName+"result"
        LoopholesList.append("1")#每调用一次就往列表中写入一个数字这样可以知道结果又多少个漏洞
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.FilePath = os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\"+self.FileName + ".txt"#不需要输入后缀，只要名字就好
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.FilePath = os.path.split(os.path.realpath(__file__))[0] + "/ScanResult/" +self.FileName+ ".txt"  # 不需要输入后缀，只要名字就好
        with open(self.FilePath, 'w+',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(Medusa+"\n")


class AgentHeader:#使用随机头类
    def result(self,Values):#使用随机头传入传入参数
        try:
            self.Values = Values
            ua = UserAgent(cache=True)
            if self.Values.lower()=="None":#如果参数为空使用随机头
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
            return "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"#报错使用随机头


class NmapScan:#扫描端口类
    def __init__(self,Url):
        Host=IpProcess(Url)#调用IP处理函数
        self.Host= Host#提取后的网址或者IP
        #self.Port = "445"#测试
        self.Port = "1-65535"#如果用户没输入就扫描全端口

    def ScanPort(self):
        try:
            Nmap = nmap.PortScanner()
            ScanResult = Nmap.scan(self.Host, self.Port, '-sV')
            HostAddress= re.compile('{\'([\d.]+)\': {').findall(str(ScanResult['scan']))[0]#只能用正则取出ip的值
            for port in ScanResult['scan'][HostAddress]['tcp']:
                Nmaps=ScanResult['scan'][HostAddress]['tcp'][port]
                NmapDB(Nmaps,port,self.Host,HostAddress).Write()
        except IOError:
             print("Please enter the correct nmap scan command.")

#为每个任务加个唯一的加密ID然后存入，后面和读取数据库后进行全量端口爆破做铺垫
class NmapDB:#NMAP的数据库
    def __init__(self,Nmap,port,ip,domain):
        self.state = Nmap['state']  # 端口状态
        self.reason = Nmap['reason']  # 端口回复
        self.name = Nmap['name']  #  	服务名称
        self.product = Nmap['product']  # 服务器类型
        self.version = Nmap['version']  # 版本
        self.extrainfo = Nmap['extrainfo']  # 其他信息
        self.conf = Nmap['conf']  # 配置
        self.cpe = Nmap['cpe']  # 消息头
        self.port = port  # 有哪些端口
        self.ip = ip  # 扫描的目标
        self.domain=domain #域名
        # 如果数据库不存在的话，将会自动创建一个 数据库
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Nmap\
                        (domain TEXT,\
                        ip TEXT,\
                        port TEXTL,\
                        state TEXT,\
                        name TEXT,\
                        product TEXT,\
                        reason TEXT,\
                        version TEXT,\
                        extrainfo TEXT,\
                        conf TEXT,\
                        cpe TEXT)")
        except:
            pass

    def Write(self):
        try:

            #sql_insert = """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe)
            self.cur.execute("""INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass

class NmapRead:#读取Nmap扫描后的数据
    def __init__(self,id):
        self.id = id  # 每个任务唯一的ID值
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        self.cur = self.con.cursor()
    def Read(self):
        try:
            port_list=[]
            self.cur.execute("select * from Nmap where id =?", (self.id,))
            values = self.cur.fetchall()
            for i in values:
                if i[3]=="open":
                    port_list.append(i[2])#发送端口号到列表中
            self.con.close()
            return port_list
        except:
            pass

class SessionKey:
    def __init__(self,username,session_key,session_time):
        self.username=username
        self.session_key=session_key
        self.session_time=session_time
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE session_key\
                        (username TEXT PRIMARY KEY,\
                        session_key TEXT,\
                        session_time TEXTL)")
        except:
            pass
    def write(self):#把验证后的两个session写入数据库中
        try:

            # sql_insert = """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe)
            self.cur.execute("""INSERT INTO session_key (username,session_key,session_time) VALUES (?,?,?)""",(self.username, self.session_key, self.session_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def read(self):#对传入的两个session进行验证
        try:
            self.cur.execute("select * from session_key where username =?", (self.username,))
            values = self.cur.fetchall()
            for i in values:
                if i[0]==self.username and self.session_key==i[1] and self.session_time==i[2]:
                    self.con.close()
                    return 1
            self.con.close()
            return 0
        except:
            return 0
class BlastingDB:#数据库爆破模块，到时候要重写移除这里
    def __init__(self,DataBaseUserFileName,DataBasePasswrodFileName):
        self.DataBaseUserFileName=DataBaseUserFileName
        self.DataBasePasswrodFileName = DataBasePasswrodFileName
    def BoomDB(self,Url):
        global BoomDBFileName
        try:
            if self.DataBaseUserFileName!=None and self.DataBasePasswrodFileName!=None:
                with open(self.DataBaseUserFileName, encoding='utf-8') as f:
                    for UserLine in tqdm(f,ascii=True,desc="DatabaseBlastingProgress:"):
                        User = UserLine
                        with open(self.DataBasePasswrodFileName, encoding='utf-8') as fp:
                            for PassWrodLine in tqdm(fp,desc="Single user password progress",ascii=True):
                                PassWrod = PassWrodLine
                                try:
                                    Url=IpProcess(Url)
                                    conn = pymysql.connect(Url, User, PassWrod, 'mysql', 3306)
                                    conn.close()
                                    if sys.platform == "win32" or sys.platform == "cygwin":
                                        BoomDBFileName = os.path.split(os.path.realpath(__file__))[
                                                             0] + "\\ScanResult\\BoomDBOutputFile.txt"
                                    elif sys.platform == "linux" or sys.platform == "darwin":
                                        BoomDBFileName = os.path.split(os.path.realpath(__file__))[0]+"/ScanResult/BoomDBOutputFile.txt"
                                    with open(BoomDBFileName, 'a', encoding='utf-8') as fg:
                                        fg.write("Database address:"+Url +"      Account:"+User+"      Passwrod:"+PassWrod+ "\n")  # 写入单独的扫描结果文件中
                                except Exception as e:
                                    pass
        except IOError:
            print("Input file content format is incorrect")
        try:
            if self.DataBaseUserFileName == None or self.DataBasePasswrodFileName==None:
                with open(os.path.split(os.path.realpath(__file__))[0]+"\\Dictionary\\MysqlUser.txt", encoding='utf-8') as f:#打开默认的User文件
                    for UserLine in tqdm(f,ascii=True,desc="Total progress of the blasting database:"):
                        User = UserLine
                        with open(os.path.split(os.path.realpath(__file__))[0]+"/Dictionary/MysqlPasswrod.txt", encoding='utf-8') as fp:#打开默认的密码文件
                            for PassWrodLine in tqdm(fp,desc="Single user password progress",ascii=True):
                                PassWrod = PassWrodLine
                                try:
                                    Url = IpProcess(Url)
                                    conn = pymysql.connect(Url, User, PassWrod, 'mysql', 3306)
                                    conn.close()
                                    if sys.platform == "win32" or sys.platform == "cygwin":
                                        BoomDBFileName = os.path.split(os.path.realpath(__file__))[
                                                             0] + "\\ScanResult\\BoomDBOutputFile.txt"
                                    elif sys.platform == "linux" or sys.platform == "darwin":
                                        BoomDBFileName = os.path.split(os.path.realpath(__file__))[0]+"/ScanResult/BoomDBOutputFile.txt"
                                    with open(BoomDBFileName, 'a', encoding='utf-8') as fg:
                                        fg.write("Database address:"+Url +"      Account:"+User+"      Passwrod:"+PassWrod+ "\n")  # 写入单独的扫描结果文件中
                                except Exception as e:
                                    pass
        except IOError:
            print("Input file content format is incorrect")



# class Proxy:#IP代理池参数
#     def __init__(self):
#         self.HttpIp=[]
#     def HttpIpProxy(self):
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                           "Chrome/59.0.3071.115 Safari/537.36"}
#         for i in tqdm(range(1,3),desc="ProxyPoolProgress",ascii=True):
#             HttpUrl = 'http://www.xicidaili.com/wt/{0}'.format(i)
#             req = requests.get(url=HttpUrl, headers=headers,timeout=10)
#             selector = Selector(text=req.text)
#             HttpAllTrs = selector.xpath('//*[@id="ip_list"]//tr')
#
#             HttpIpLists = []
#             for tr in HttpAllTrs[1:]:#过滤第一个tr标签里面是其他数据
#                 HttpIp = tr.xpath('td[2]/text()').extract()[0]
#                 HttpPort = tr.xpath('td[3]/text()').extract()[0]
#                 #proxy_type = tr.xpath('td[6]/text()').extract()[0].lower()
#                 HttpIpLists.append((HttpIp+':'+HttpPort))#存储到httpIP列表里面
#
#             for ip in tqdm(HttpIpLists,ascii=True,desc="Cleaning page %s IP"%i):
#                 #print(ip)
#                 proxies = {
#                     "http": "http://"+str(ip)#使用代理前面一定要加http://或者https://
#                 }
#                 try:
#
#                     if requests.get('https://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200:
#                         if ip not in self.HttpIp:#如果代理IP不在列表里面就传到列表里
#                             global f
#                             if sys.platform == "win32" or sys.platform == "cygwin":
#                                 f = open(os.path.split(os.path.realpath(__file__))[0] + "\\ScanResult\\ProxyPool.txt",
#                                          'a+', encoding='utf-8')
#                             elif sys.platform == "linux" or sys.platform == "darwin":
#                                 f = open(os.path.split(os.path.realpath(__file__))[0]+"/ScanResult/ProxyPool.txt", 'a+', encoding='utf-8')
#                             ip=ip+"\r"
#                             f.write(str(ip) ) # 写入单独的扫描结果文件中
#                             f.close()
#                             self.HttpIp.append(ip)
#                 except:
#                     pass
class ReadVulnerability:
    pass
class VulnerabilityDetails:
    def __init__(self,medusa,url):
        try:
            self.url = str(url)  # 目标域名
            self.name=medusa['name']#漏洞名称
            self.number = medusa['number']  # CVE编号
            self.author = medusa['author'] # 插件作者
            self.createDate = medusa['createDate']  # 插件编辑时间
            self.algroup = medusa['algroup']  # 插件名称
            self.rank = medusa['rank'] # 漏洞等级
            self.disclosure = medusa['disclosure']  # 漏洞披露时间，如果不知道就写编写插件的时间
            self.details=medusa['details']# 结果
            self.affects=medusa['affects']# 漏洞组件
            self.desc_content=medusa['desc_content']# 漏洞描述
            self.suggest=medusa['suggest']# 修复建议
            self.version = medusa['version']  # 漏洞影响的版本
            # 如果数据库不存在的话，将会自动创建一个 数据库
            if sys.platform == "win32" or sys.platform == "cygwin":
                self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
            elif sys.platform == "linux" or sys.platform == "darwin":
                self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0]+"/Medusa.db")
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                #如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Medusa\
                            (id INTEGER PRIMARY KEY,\
                            url TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            affects TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            suggest TEXT NOT NULL,\
                            desc_content TEXT NOT NULL,\
                            details TEXT NOT NULL,\
                            number TEXT NOT NULL,\
                            author TEXT NOT NULL,\
                            createDate TEXT NOT NULL,\
                            disclosure TEXT NOT NULL,\
                            algroup TEXT NOT NULL,\
                            version TEXT NOT NULL)")
            except:
                pass
        except:
            pass
    def Write(self):
        try:
            self.cur.execute("""INSERT INTO Medusa (url,name,affects,rank,suggest,desc_content,details,number,author,createDate,disclosure,algroup,version) \
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",(self.url,self.name,self.affects,self.rank,self.suggest,self.desc_content,self.details,self.number,self.author,self.createDate,self.disclosure,self.algroup,self.version,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass



class VulnerabilityInquire:
    def __init__(self,pid):#先通过id查，后面要是有用户ID 再运行的时候创建一个用户信息的表或者什么的到时候再说
        self.id=pid
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Inquire(self):
        self.cur.execute("select * from Medusa where id =?",self.id)
        values = self.cur.fetchall()
        json_values={}
        for i in values:
            json_values["id"]=i[0]
            json_values["name"] =i[1]
            json_values["affects"] =i[2]
            json_values["rank"] =i[3]
            json_values["suggest"] =i[4]
            json_values["desc_content"] =i[5]
            json_values["details"] =i[6]
        self.con.close()
        return json_values

class login:#登录
    def __init__(self,username):
        self.username=username
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def logins(self):#根据数据进行查询用户名和数据库是否相等
        self.cur.execute("select * from user_info where user =?",(self.username,))
        values = self.cur.fetchall()
        try:
            global passwd
            for i in values:
                passwd= i[1]#获取密码
            if passwd!=None:#判断是否在数据库中
                self.con.close()
                return passwd
        except:
            return 0
class register:#注册
    def __init__(self,username,password,emil):
        self.username = username  # 用户名
        self.password = password # 密码
        self.emil=emil#邮箱
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE user_info(user TEXT PRIMARY KEY,password TEXT NOT NULL,emil TEXT NOT NULL)")
        except:
            pass
    def register_write(self):
        try:

            self.cur.execute("INSERT INTO user_info(user,password,emil)VALUES (?,?,?)",(self.username, self.password , self.emil,))
            # 提交
            self.con.commit()
            self.con.close()
            return 1#返回真或者假
        except:
            return 0
    def register_inquire_emil(self):#根据数据进行查询判断emil
        self.cur.execute("select * from user_info where emil =?",(self.emil,))
        values = self.cur.fetchall()
        try:
            global emil
            for i in values:
                emil= i[2]#判断传入的邮箱是否在数据库中
            if str(emil) == str(self.emil):#判断是否在数据库中
                self.con.close()
                return 1
        except:
            return 0
    def register_inquire_user(self):#根据数据进行查询判断user
        self.cur.execute("select * from user_info where user =?",(self.username,))
        values = self.cur.fetchall()
        try:
            global user
            for i in values:
                user= i[0]
            if str(user) == str(self.username):  # 判断是否在数据库中
                self.con.close()
                return 1
        except:
            return 0

class ErrorLog:#报错写入日志
    def __init__(self):
        global filename
        if sys.platform == "win32" or sys.platform == "cygwin":
            filename=os.path.split(os.path.realpath(__file__))[0]+'\\my.log'#获取当前文件所在的目录，即父目录
        elif sys.platform == "linux" or sys.platform == "darwin":
            filename = os.path.split(os.path.realpath(__file__))[0] + '/my.log'  # 获取当前文件所在的目录，即父目录
        #filename=os.path.realpath(__file__)#获取当前文件名
        log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,
                            format=log_format)  # 初始化配置信息
    def Write(self,url,name):
        logging.info(url)
        logging.warning(name)

class Dnslog:#Dnslog判断
    def __init__(self):
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt=""
        for i in range(15):
            salt += random.choice(H)
        self.host=str(salt+".medusa.ascotbe.com")
    def dns_host(self):
        return self.host
    def result(self):
        data=json.dumps({"domain": self.host})
        try:
            status = requests.post('http://log.ascotbe.com/api/validate', timeout=2,data=data)
            code=status.status_code
            if code == 200:
                return True
            else:
                return False
        except Exception:
            ErrorLog().Write(self.host,"Dnslog")


class Ysoserial:
    def __init__(self):
        system_type=sys.platform
        if system_type=="win32" or system_type=="cygwin":
            self.ysoserial=os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "."),'Dictionary\\ysoserial.jar')
        elif system_type=="linux" or system_type=="darwin":
            self.ysoserial= os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "."),'Dictionary/ysoserial.jar')
    def result(self):
        return self.ysoserial
    
class randoms:#生成随机数
    def result(self,nub):
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
class UrlProcessing:#URL处理函数
    def result(self,url):
        if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port

class ThreadPool:#线程池，所有插件都发送过来一起调用
    def __init__(self):
        self.ThreaList=[]#存放线程列表
        self.text=0#统计线程数
    def Append(self,plugin,url,Values,ProxyIp):
        self.text+=1
        ua = AgentHeader().result(Values)
        self.ThreaList.append(threading.Thread(target=plugin, args=(url,ua,ProxyIp)))
    def SubdomainAppend(self,plugin,Url,SubdomainJudge):
        self.ThreaList.append(threading.Thread(target=plugin, args=(Url, SubdomainJudge)))
    def NmapAppend(self,plugin,Url):
        self.ThreaList.append(threading.Thread(target=plugin, args=(Url)))
    def Start(self,ThreadNumber):
        for t in tqdm(self.ThreaList,ascii=True,desc="\033[1;40;32m[ + ] Medusa scan progress bar\033[0m"): # 开启列表中的多线程
            #t.setDaemon(True)
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for p in tqdm(self.ThreaList,ascii=True,desc="\033[1;40;32m[ + ] Medusa cleanup thread progress\033[0m"):
            p.join()
            #self.off=t.isAlive()
        self.ThreaList.clear()#清空列表，防止多次调用导致重复使用
        print("\033[1;40;31m[ ! ] Scan is complete, please see the ScanResult file\033[0m")

class Prompt:#输出横幅，就是每个组件加载后输出的东西
    def __init__(self,name):
        self.name=name
        print("\r\033[1;40;32m[ + ] Loading attack module:\033[0m"+"\033[1;40;35m {}             \033[0m".format(self.name),end='')#这样能覆盖前面输出的内容
        time.sleep(0.3)
