#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import time
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
        FileNames = os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\"+self.FileName + ".txt"#不需要输入后缀，只要名字就好
        with open(FileNames, 'w+',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(Medusa+"\n")



class UserAgentS:#使用随机头类
    def __init__(self,Values):
        self.Values=Values

    def UserAgent(self):#使用随机头传入传入参数
        try:
            ua = UserAgent(verify_ssl=False)
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
        self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
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

            sql_insert = """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe)
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass


class BlastingDB:
    def __init__(self,DataBaseUserFileName,DataBasePasswrodFileName):
        self.DataBaseUserFileName=DataBaseUserFileName
        self.DataBasePasswrodFileName = DataBasePasswrodFileName
    def BoomDB(self,Url):
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
                                    BoomDBFileName = os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\BoomDBOutputFile.txt"
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
                                    BoomDBFileName = os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\BoomDBOutputFile.txt"
                                    with open(BoomDBFileName, 'a', encoding='utf-8') as fg:
                                        fg.write("Database address:"+Url +"      Account:"+User+"      Passwrod:"+PassWrod+ "\n")  # 写入单独的扫描结果文件中
                                except Exception as e:
                                    pass
        except IOError:
            print("Input file content format is incorrect")



class Proxy:#IP代理池参数
    def __init__(self):
        self.HttpIp=[]
    def HttpIpProxy(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/59.0.3071.115 Safari/537.36"}
        for i in tqdm(range(1,3),desc="ProxyPoolProgress",ascii=True):
            HttpUrl = 'http://www.xicidaili.com/wt/{0}'.format(i)
            req = requests.get(url=HttpUrl, headers=headers,timeout=10)
            selector = Selector(text=req.text)
            HttpAllTrs = selector.xpath('//*[@id="ip_list"]//tr')

            HttpIpLists = []
            for tr in HttpAllTrs[1:]:#过滤第一个tr标签里面是其他数据
                HttpIp = tr.xpath('td[2]/text()').extract()[0]
                HttpPort = tr.xpath('td[3]/text()').extract()[0]
                #proxy_type = tr.xpath('td[6]/text()').extract()[0].lower()
                HttpIpLists.append((HttpIp+':'+HttpPort))#存储到httpIP列表里面

            for ip in tqdm(HttpIpLists,ascii=True,desc="Cleaning page %s IP"%i):
                #print(ip)
                proxies = {
                    "http": "http://"+str(ip)#使用代理前面一定要加http://或者https://
                }
                try:

                    if requests.get('https://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200:
                        if ip not in self.HttpIp:#如果代理IP不在列表里面就传到列表里
                            f = open(os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\ProxyPool.txt", 'a+', encoding='utf-8')
                            ip=ip+"\r"
                            f.write(str(ip) ) # 写入单独的扫描结果文件中
                            f.close()
                            self.HttpIp.append(ip)
                except:
                    pass
class VulnerabilityDetails:

    def __init__(self,medusa):

        try:
            self.name=medusa['name']#漏洞名称
            self.details=medusa['details']# 结果
            self.affects=medusa['affects']# 漏洞组件
            self.desc_content=medusa['desc_content']# 漏洞描述
            self.suggest=medusa['suggest']# 修复建议
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0]+"\\Medusa.db")
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # self.cur.execute("CREATE TABLE Medusa\
                #             (id INTEGER PRIMARY KEY,\
                #             name TEXT NOT NULL,\
                #             affects TEXT NOT NULL,\
                #             rank TEXT NOT NULL,\
                #             suggest TEXT NOT NULL,\
                #             desc_content TEXT NOT NULL,\
                #             details TEXT NOT NULL)")
                #如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Medusa\
                            (id TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            affects TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            suggest TEXT NOT NULL,\
                            desc_content TEXT NOT NULL,\
                            details TEXT NOT NULL)")
            except:
                pass
        except:
            pass
    def serious(self):
        try:

            sql_insert = """INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
    VALUES (4,'{}','{}','严重','{}','{}','{}')""".format(self.name,self.affects,self.suggest,self.desc_content,self.details)
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def High(self):
         # 使用cursor()方法获取操作游标
        try:
            sql_insert = """INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
    VALUES (5,'{}','{}','高危','{}','{}','{}')""".format(self.name,
                                                                                                        self.affects,
                                                                                                        self.suggest,
                                                                                                        self.desc_content,
                                                                                                        self.details)
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def Intermediate(self):
         # 使用cursor()方法获取操作游标
        try:
            sql_insert = """INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
    VALUES (4,'{}','{}','中危','{}','{}','{}')""".format(self.name,self.affects,self.suggest,self.desc_content,self.details)
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def Low(self):
         # 使用cursor()方法获取操作游标
        try:
            sql_insert = """INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
    VALUES (4,'{}','{}','低危','{}','{}','{}')""".format(self.name,self.affects,self.suggest,self.desc_content,self.details)
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass


class VulnerabilityInquire:#还要小BUG
    def __init__(self,pid):#先通过id查，后面要是有用户ID 再运行的时候创建一个用户信息的表或者什么的到时候再说
        self.id=pid
        self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Inquire(self):
        sql = "select * from Medusa where id ='"+self.id+"'"
        self.cur.execute(sql)
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




class ErrorLog:
    def __init__(self):
        filename=os.path.split(os.path.realpath(__file__))[0]+'\\my.log'#获取当前文件所在的目录，即父目录
        #filename=os.path.realpath(__file__)#获取当前文件名
        log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,
                            format=log_format)  # 初始化配置信息
    def Write(self,url,name):
        logging.info(url)
        logging.warning(name)

