#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import urllib.parse
import requests
import sqlite3
from tqdm import tqdm
import logging
import os
import re
import socket
import base64
import random
import sys
import time
import multiprocessing
from typing import List, Tuple
import threading
import subprocess
import hashlib
from config import ceye_dnslog_url, ceye_dnslog_key, debug_mode,dnslog_name,port_threads_number,port_timeout_period,thread_timeout_number,user_agent_browser_type
import copy
#########
# 全局变量
WriteFileUnixTimestamp = str(int(time.time()))


#########

def IpProcess(Url: str) -> str:
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)




class Proxies:  # 代理处理函数
    def result(self, proxies_ip: str or None):
        try:
            if proxies_ip == None:
                return proxies_ip
            else:
                return {"http": "http://{}".format(proxies_ip), "https": "https://{}".format(proxies_ip)}
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Proxies(class)_result(def)", e)
            return None#报错就返回空



class WriteFile:  # 写入文件类
    def result(self, TargetName: str, Medusa: str) -> None:
        #需要对传入的完整URL进行提取后进行拼接
        self.FileName = time.strftime("%Y-%m-%d", time.localtime()) + "_" + UrlProcessing().result(TargetName)[1] + "_" + WriteFileUnixTimestamp
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.FilePath = GetRootFileLocation().Result()+ "\\ScanResult\\" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        elif sys.platform == "linux" or sys.platform == "darwin":
            self.FilePath = GetRootFileLocation().Result() + "/ScanResult/" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        with open(self.FilePath, 'a+', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(Medusa + "\n")

class AgentHeader:  # 使用随机头类
    def result(self) -> str:  # 使用随机头传入传入参数
        try:
            self.Values = user_agent_browser_type
            ua = UserAgent(verify_ssl=False)
            if self.Values == None:  # 如果参数为空使用随机头
                return (ua.random)
            elif self.Values.lower() == "firefox":  # 如果是火狐字符串使用火狐头
                return (ua.firefox)
            elif self.Values.lower() == "ie":  # IE浏览器
                return (ua.ie)
            elif self.Values.lower() == "msie":  # msie
                return (ua.msie)
            elif self.Values.lower() == "opera":  # Opera Software
                return (ua.opera)
            elif self.Values.lower() == "chrome":  # 谷歌浏览器
                return (ua.chrome)
            elif self.Values.lower() == "AppleWebKit":  # AppleWebKit
                return (ua.google)
            elif self.Values.lower() == "Gecko":  # Gecko
                return (ua.ff)
            elif self.Values.lower() == "safari":  # apple safari
                return (ua.safari)
            else:
                return (ua.random)  # 如果用户瞎几把乱输使用随机头
        except Exception as e:
            ErrorLog().Write("ClassCongregation_AgentHeader(class)_result(def)", e)
            return "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"  # 报错使用随机头


class GetDatabaseFilePath:  # 主数据库文件路径返回值
    def result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "\\Medusa.db"
            return DatabaseFilePath
        elif sys.platform == "linux" or sys.platform == "darwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "/Medusa.db"
            return DatabaseFilePath


class PortScan:  # 扫描端口类
    def __init__(self):
        try:

            self.CustomizePortList =[] # 用户输入处理后的列表
            self.DefaultPortList = [20, 21, 22, 23, 53,80, 161, 389, 443, 873, 1025, 1099, 2222, 2601, 2604, 3312, 3311, 4440, 5900, 5901,
                       5902, 7002, 9000, 9200, 10000, 50000, 50060, 50030, 8080, 139, 445, 3389, 13389, 7001, 1521, 3306,
                       1433, 5000, 5432, 27017, 6379, 11211]  # 常用端口扫描列表
            self.OpenPorts=[]
        except Exception as e:
            ErrorLog().Write("ClassCongregation_PortScan(class)___init__(def)", e)


    def PortTest(self,**kwargs):
        port = int(kwargs.get("port"))

        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((self.Ip, port))
            sk.settimeout(port_timeout_period)
            sk.close()
            self.OpenPorts.append(str(port))  # 传入列表中
            #成功直接调用写入端口函数

        except Exception as e:
            pass
    def Start(self,**kwargs):
        #传入端口列表，主函数中写入
        PortInformation = kwargs.get("PortInformation")
        PortType = kwargs.get("PortType")
        Uid=kwargs.get("Uid")
        Url = kwargs.get("Url")
        self.Host = IpProcess(Url)  # 调用IP处理函数,获取URL或者IP
        self.Ip = socket.gethostbyname(self.Host)  # 如果是URL会进行二次处理获取到IP
        ActiveScanId=kwargs.get("ActiveScanId")
        self.PortHandling(PortInformation,PortType)
        try:
            Pool = ThreadPool()
            for Port in self.CustomizePortList:
                Pool.Append(self.PortTest, port=Port)

            Pool.Start(port_threads_number)  # 启动线程池
            #print(self.OpenPorts)
            #调用写入数据库函数和调用写入文件函数
            CreationTime=str(int(time.time()))
            for i in self.OpenPorts:#循环写入到数据库中
                PortDB(uid=Uid,active_scan_id=ActiveScanId,ip=self.Ip,domain=self.Host,creation_time=CreationTime,port=i).Write()#写到数据库中
                WriteFile().result(TargetName=self.Host+"_Port",Medusa=self.Ip+":"+i+"\n")#写到文件中
        except Exception as e:
            ErrorLog().Write("ClassCongregation_PortScan(class)_Start(def)", e)


    def PortHandling(self,PortInformation,PortType):  # 进行正则匹配处理
        try:
            Pattern = re.compile(r'\d*')  # 查找数字
            RegularResult = Pattern.findall(PortInformation)
            if PortType == 1:  # 处理为范围类型数据
                ExtractContent = []  # 剔除空字节内容和超过最大端口数据
                for i in RegularResult:
                    if i != "" and int(i) <= 65535:
                        ExtractContent.append(i)
                PortStart = int(ExtractContent[0])  # 起始端口
                PortEnd = int(ExtractContent[1])  # 起始端口
                if PortEnd < PortStart:  # 如果用户输入错误为大的在前面小的在后面的话
                    tmp = PortEnd
                    PortEnd = PortStart
                    PortStart = tmp
                for Port in range(PortStart, PortEnd + 1):
                    self.CustomizePortList.append(Port)
            if PortType == 2:  # 处理为字典类型数据
                for Port in RegularResult:
                    if Port != "" and int(Port) <= 65535:
                        self.CustomizePortList.append(Port)
            if PortType == 3:  # 使用默认字典
                self.CustomizePortList=self.DefaultPortList
        except Exception as e:
            self.CustomizePortList = self.DefaultPortList#如果报错直接使用默认端口进行扫描
            ErrorLog().Write("ClassCongregation_PortScan(class)_PortHandling(def)", e)




class PortDB:  # 端口数据表
    def __init__(self,**kwargs):
        self.uid = kwargs.get("uid") # 用户UID
        self.active_scan_id = kwargs.get("active_scan_id")  # 扫描active_scan_id
        self.port = kwargs.get("port")  # 开放端口
        self.ip = kwargs.get("ip")  # 目标IP
        self.domain = kwargs.get("domain") # 目标域名
        self.creation_time=kwargs.get("creation_time") # 创建时间
        # 如果数据库不存在的话，将会自动创建一个 数据库
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE PortInfo\
                            (port_info_id INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL,\
                            port TEXT NOT NULL,\
                            ip TEXT NOT NULL,\
                            domain TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("ClassCongregation_PortDB(class)_init(def)", e)

    def Write(self):
        try:
            self.cur.execute(
                """INSERT INTO PortInfo (uid,active_scan_id,port,ip,domain,creation_time) VALUES (?,?,?,?,?,?)""",
                (self.uid, self.active_scan_id,self.port, self.ip, self.domain, self.creation_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_PortDB(class)_Write(def)", e)

    def Query(self, **kwargs):
            Uid = kwargs.get("uid")
            ActiveScanId = kwargs.get("active_scan_id")
            try:
                self.cur.execute("select * from PortInfo where active_scan_id =? and uid=?", (ActiveScanId, Uid,))
                result_list = []  # 存放json的返回结果列表用
                for i in self.cur.fetchall():
                    JsonValues = {}
                    # JsonValues["active_scan_id"] = i[2]
                    JsonValues["port"] = i[3]
                    JsonValues["ip"] = i[4]
                    JsonValues["domain"] = i[5]
                    JsonValues["creation_time"] = i[6]
                    result_list.append(JsonValues)
                self.con.close()
                return result_list
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_QueryTokenValidity(def)", e)
                return None



class GithubCveApi:  # CVE写入表
    def __init__(self,**kwargs):
        try:
            self.cve_id = kwargs.get("id")  # 唯一的ID
            self.cve_name = kwargs.get("name")   # 名字
            self.cve_html_url = kwargs.get("html_url")    # 链接
            self.cve_created_at = kwargs.get("created_at")  # 创建时间
            self.cve_updated_at = kwargs.get("updated_at")  # 更新时间
            self.cve_pushed_at = kwargs.get("pushed_at")  # push时间
            self.cve_forks_count = kwargs.get("forks_count")  # fork人数
            self.cve_watchers_count =kwargs.get("watchers_count")  # star人数
            self.cve_write_time = str(int(time.time()))  # 写入时间
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表

            # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
            self.cur.execute("CREATE TABLE GithubMonitor\
                        (id INTEGER PRIMARY KEY,\
                        github_id TEXT NOT NULL,\
                        name TEXT NOT NULL,\
                        html_url TEXT NOT NULL,\
                        created_at TEXT NOT NULL,\
                        updated_at TEXT NOT NULL,\
                        pushed_at TEXT NOT NULL,\
                        forks_count TEXT NOT NULL,\
                        watchers_count TEXT NOT NULL,\
                        write_time TEXT NOT NULL,\
                        update_write_time TEXT NOT NULL)")
        except Exception as e:
            pass
            #ErrorLog().Write("ClassCongregation_GithubCveApi(class)_init(def)", e)

    def Write(self):
        try:
            self.cur.execute("""INSERT INTO GithubMonitor (github_id,name,html_url,created_at,updated_at,pushed_at,forks_count,watchers_count,write_time,update_write_time) \
    VALUES (?,?,?,?,?,?,?,?,?,?)""", (
            self.cve_id, self.cve_name, self.cve_html_url, self.cve_created_at, self.cve_updated_at, self.cve_pushed_at,
            self.cve_forks_count, self.cve_watchers_count, self.cve_write_time, self.cve_write_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
                ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Write(def)", e)

    def Update(self):
        UpdateTime=str(int(time.time()))
        try:
            self.cur.execute(
                """UPDATE GithubMonitor SET forks_count = ?,updated_at=?,pushed_at=?,watchers_count=?,update_write_time=?  WHERE github_id = ?""",
                (self.cve_forks_count, self.cve_updated_at, self.cve_pushed_at, self.cve_watchers_count,
                 UpdateTime, self.cve_id,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Update(def)", e)

    def Judgment(self) -> bool:#用于判断是否更新
        try:
            self.cur.execute(
                """SELECT * FROM GithubMonitor WHERE github_id=?""", (self.cve_id,))
            values = self.cur.fetchall()
            cve_query_results = True
            if len(values) == 0:
                cve_query_results = False
            else:
                cve_query_results = True
            # 提交
            self.con.commit()
            self.con.close()
            return cve_query_results
        except Exception as e:
            ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Judgment(def)", e)

    def Query(self):#用于判断是否更新
        try:
            ProcessedData=[]
            self.cur.execute(
                """SELECT * FROM GithubMonitor""")
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["github_id"]= i[1]
                JsonValues["name"]= i[2]
                JsonValues["html_url"]= i[3]
                JsonValues["created_at"]= i[4]
                JsonValues["updated_at"]= i[5]
                JsonValues["pushed_at"]= i[6]
                JsonValues["forks_count"]= i[7]
                JsonValues["watchers_count"]= i[8]
                ProcessedData.append(JsonValues)
            return ProcessedData
        except Exception as e:
            ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Query(def)", e)


class VulnerabilityDetails:  # 所有数据库写入都是用同一个类
    def __init__(self, medusa,request, **kwargs):
        try:
            self.url = str(kwargs.get("Url"))  # 目标域名，如果是代理扫描会有完整的路径
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.name = medusa['name']  # 漏洞名称
            self.number = medusa['number']  # CVE编号
            self.author = medusa['author']  # 插件作者
            self.create_date = medusa['create_date']  # 插件创建时间
            self.algroup = medusa['algroup']  # 插件名称
            self.rank = medusa['rank']  # 漏洞等级
            self.disclosure = medusa['disclosure']  # 漏洞披露时间，如果不知道就写编写插件的时间
            self.details = base64.b64encode(medusa['details'].encode(encoding="utf-8")).decode('utf-8')  # 对结果进行编码写入数据库，鬼知道数据里面有什么玩意
            self.affects = medusa['affects']  # 漏洞组件
            self.desc_content = medusa['desc_content']  # 漏洞描述
            self.suggest = medusa['suggest']  # 修复建议
            self.version = medusa['version']  # 漏洞影响的版本
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.active_scan_id = kwargs.get("ActiveScanId")  # 传入的父表SID
            try:
                self.response_headers=base64.b64encode(str(request.headers).encode(encoding="utf-8")).decode(encoding="utf-8") # 响应头base64加密后数据
                self.response_text=base64.b64encode(str(request.text).encode(encoding="utf-8")).decode(encoding="utf-8")  # 响应返回数据包
                self.response_byte=base64.b64encode(request.content).decode(encoding="utf-8")#响应返回byte类型数据包
                self.response_status_code=str(request.status_code) # 响应状态码
                self.request_path_url=str(request.request.path_url)  # 请求路径
                self.request_body=base64.b64encode(str(request.request.body).encode(encoding="utf-8")).decode(encoding="utf-8")  # 请求的POST请求数据
                self.request_method=str(request.request.method)  # 请求方式
                self.request_headers=base64.b64encode(str(request.request.headers).encode(encoding="utf-8")).decode(encoding="utf-8")  # 请求头
            except:
                #如果报错就爆数据全部置空
                self.response_headers = ""
                self.response_text = ""
                self.response_byte = ""
                self.response_status_code = ""
                self.request_path_url = ""
                self.request_body = ""
                self.request_method = ""
                self.request_headers = ""

            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Medusa\
                            (scan_info_id INTEGER PRIMARY KEY,\
                            url TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            affects TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            suggest TEXT NOT NULL,\
                            desc_content TEXT NOT NULL,\
                            details TEXT NOT NULL,\
                            number TEXT NOT NULL,\
                            author TEXT NOT NULL,\
                            create_date TEXT NOT NULL,\
                            disclosure TEXT NOT NULL,\
                            algroup TEXT NOT NULL,\
                            version TEXT NOT NULL,\
                            timestamp TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            response_headers TEXT NOT NULL,\
                            response_text TEXT NOT NULL,\
                            response_byte TEXT NOT NULL,\
                            response_status_code TEXT NOT NULL,\
                            request_path_url TEXT NOT NULL,\
                            request_body TEXT NOT NULL,\
                            request_method TEXT NOT NULL,\
                            request_headers TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Medusa (url,name,affects,rank,suggest,desc_content,details,number,author,create_date,disclosure,algroup,version,timestamp,active_scan_id,uid,response_headers,response_text,response_byte,response_status_code,request_path_url,request_body,request_method,request_headers) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
                self.url, self.name, self.affects, self.rank, self.suggest, self.desc_content, self.details,
                self.number,
                self.author, self.create_date, self.disclosure, self.algroup, self.version, self.timestamp,
                self.active_scan_id,self.uid,self.response_headers,self.response_text,self.response_byte,self.response_status_code,self.request_path_url,self.request_body,self.request_method,self.request_headers,))
            # 提交
            GetSsid = self.cur.lastrowid
            self.con.commit()
            self.con.close()
            ScanInformation().Write(scan_info_id=GetSsid,url=self.url,active_scan_id=self.active_scan_id,rank=self.rank,uid=self.uid,name=self.name)#调用web版数据表，写入ScanInformation关系表
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_Write(def)", e)

class ErrorLog:  # 报错写入日志
    def __init__(self):
        global filename
        LogDate=time.strftime("%Y-%m-%d", time.localtime())
        if sys.platform == "win32" or sys.platform == "cygwin":
            filename = os.path.split(os.path.realpath(__file__))[0] + '\\Log\\'+LogDate+'.log'  # 获取当前文件所在的目录，即父目录
        elif sys.platform == "linux" or sys.platform == "darwin":
            filename = os.path.split(os.path.realpath(__file__))[0] + '/Log/'+LogDate+'.log'  # 获取当前文件所在的目录，即父目录
        # filename=os.path.realpath(__file__)#获取当前文件名
        log_format = '%(asctime)s - %(processName)s[%(process)d] - %(levelname)s: %(message)s'
        logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,
                            format=log_format)  # 初始化配置信息

    def Write(self, Name, ErrorInfo):
        logging.info(Name)
        logging.warning(ErrorInfo)
        logging.shutdown()#通过刷新和关闭所有处理程序来通知日志记录系统执行有序的关闭。


class Dnslog:  # Dnslog判断
    def __init__(self):
        #该网站是通过PHPSESSID来判断dns归属谁的所有可以随机一个这个
        h = "abcdefghijklmnopqrstuvwxyz0123456789"
        salt_cookie = ""
        for i in range(26):
            salt_cookie += random.choice(h)
        self.headers = {
            "Cookie": "PHPSESSID="+salt_cookie
        }
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt = ""
        for i in range(15):
            salt += random.choice(H)
        try:
            self.host = str(salt + "." + self.get_dnslog_url())
        except Exception as e:
            print("\033[31m[ ! ] Unable to get dnslog, please replace ceye! \033[0m")
            self.host=""
            ErrorLog().Write("ClassCongregation_Dnslog(class)_init_(def)", e)

    def dns_host(self) -> str:
        return str(self.host)

    def get_dnslog_url(self):
        if dnslog_name=="dnslog.cn":
            try:
                self.dnslog_cn=requests.get("http://www.dnslog.cn/getdomain.php",headers=self.headers,timeout=6).text
                return self.dnslog_cn
            except Exception as e:
                ErrorLog().Write("ClassCongregation_Dnslog(class)_get_dns_log_url(def)", e)
        elif dnslog_name=="ceye":
            return ceye_dnslog_url

    def result(self) -> bool:
        # DNS判断后续会有更多的DNS判断，保持准确性
        if dnslog_name=="dnslog.cn":
            return self.dnslog_cn_dns()
        elif dnslog_name=="ceye":
            return self.ceye_dns()

    def ceye_dns(self) -> bool:
        try:
            # status = requests.post('http://log.ascotbe.com/api/validate', timeout=2,data=data)
            # code=status.status_code
            # if code == 200:
            status = requests.get("http://api.ceye.io/v1/records?token=" + ceye_dnslog_key + "&type=dns&filter=",timeout=6)
            self.ceye_dnslog_text = status.text
            if self.ceye_dnslog_text.find(self.host) != -1:  # 如果找到Key
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write(self.host+"|| ceye_dns",e)

    def dnslog_cn_dns(self) -> bool:
        try:
            status = requests.get("http://www.dnslog.cn/getrecords.php?t="+self.dnslog_cn,headers=self.headers,  timeout=6)
            self.dnslog_cn_text = status.text
            if self.dnslog_cn_text.find(self.host) != -1:  # 如果找到Key
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write(self.host + "|| dnslog_cn_dns", e)

    def dns_text(self):
        if dnslog_name=="dnslog.cn":
            return self.dnslog_cn_text
        elif dnslog_name=="ceye":
            return self.ceye_dnslog_text


class randoms:  # 生成随机数
    def result(self, nub: int) -> str:
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def LowercaseAndNumbers(self, nub: int) -> str:#生成小写和数字的值
        H = "abcdefghijklmnopqrstuvwxyz123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def Numbers(self, nub: int) -> str:#生成小写和数字的值
        H = "0123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def EnglishAlphabet(self, nub: int) -> str:#生成英文字母
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt


class UniformResourceLocatorParameterSubstitution:#对URL参数进行替换
    def Result(self,**kwargs):
        Url=kwargs.get("url")
        Vals=kwargs.get("vals")
        ret = []
        ArrayExtraction={}
        ConnectionHandling= urllib.parse.urlparse(Url).query
        PureUrl = Url.replace('?'+ConnectionHandling, '')
        ParameterExtraction = urllib.parse.parse_qs(ConnectionHandling)
        for i in ParameterExtraction.keys():#对提取的内容进行处理成json
            ParameterExtraction[i]=ParameterExtraction[i][0]
            ArrayExtraction[i]=ParameterExtraction[i]

        for k in ParameterExtraction.keys():#对每个产生进行拼接处理
            tmp_dict = copy.deepcopy(ParameterExtraction)
            tmp_dict[k] = Vals
            tmp_qs = urllib.parse.unquote(urllib.parse.urlencode(tmp_dict))
            ret.append(PureUrl + "?" + tmp_qs)
        return ret

class UrlProcessing:  # URL处理函数
    def result(self, url: str) -> Tuple[str, str, int]:
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port


class ThreadPool:  # 线程池，适用于单个插件
    def __init__(self):
        self.ThreaList = []  # 存放线程列表
        self.text = 0  # 统计线程数

    def Append(self, plugin,**kwargs):
        self.text += 1
        self.ThreaList.append(threading.Thread(target=plugin,kwargs=kwargs))

    def Start(self,ThreadNumber):
        for t in self.ThreaList:  # 开启列表中的多线程
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for p in self.ThreaList:
            p.join(thread_timeout_number)
        self.ThreaList.clear()  # 清空列表，防止多次调用导致重复使用

class ProcessPool:  # 进程池，解决pythonGIL锁问题，单核跳舞实在难受
    def __init__(self):
        self.ProcessList=[]#创建进程列表
        self.CountList = []  # 用来计数判断进程数

    def Append(self, Plugin,**kwargs):


        # Uid=kwargs.get("Uid")
        # Sid=kwargs.get("Sid")
        self.ProcessList.append(multiprocessing.Process(target=Plugin,kwargs=kwargs))

    def PortAppend(self, Plugin, **kwargs):
        self.ProcessList.append(multiprocessing.Process(target=Plugin, kwargs=kwargs))

    def Start(self, ProcessNumber):
        if debug_mode:  # 如果开了debug模式就不显示进度条
            for t in self.ProcessList:  # 开启列表中的多进程
                t.start()
                self.CountList.append(t)#发送到容器中用于判断
                while True:
                    # 判断正在运行的线程数量,如果小于5则退出while循环,
                    # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                    if len([p for p in self.CountList if p.exitcode is None])<ProcessNumber:
                        break
            for p in self.ProcessList:
                p.join()
        else:  # 如果没开Debug就改成进度条形式
            for t in tqdm(self.ProcessList, ascii=True,
                          desc="\033[32m[ + ] Medusa scan progress bar\033[0m"):  # 开启列表中的多线程
                t.start()
                while True:
                    # 判断正在运行的线程数量,如果小于5则退出while循环,
                    # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                    if len([p for p in self.CountList if p.exitcode is None]) < ProcessNumber:
                        break
            for p in tqdm(self.ProcessList, ascii=True, desc="\033[32m[ + ] Medusa cleanup thread progress\033[0m"):
                p.join()
        self.ProcessList.clear()  # 清空列表，防止多次调用导致重复使用


class Prompt:  # 输出横幅，就是每个组件加载后输出的东西
    def __init__(self, name: str):
        self.name = name
        if debug_mode:
            pass
        else:
            sizex, sizey = CommandLineWidth().getTerminalSize()
            prompt = "\033[32m[ + ] Loading attack module: \033[0m" + "\033[35m{}\033[0m".format(self.name)
            PromptSize = sizex - len(prompt) + 18#28
            FillString = ""
            for i in range(0, PromptSize):
                FillString = FillString + " "
            sys.stdout.write("\r" + prompt + FillString)
            time.sleep(0.1)
            sys.stdout.flush()


class CommandLineWidth:  # 输出横幅，就是每个组件加载后输出的东西
    def getTerminalSize(self):
        import platform  # 获取使用这个软件的平台
        current_os = platform.system()  # 获取操作系统的具体类型
        tuple_xy = None
        if current_os == 'Windows':
            tuple_xy = self._getTerminalSize_windows()
            if tuple_xy is None:
                tuple_xy = self._getTerminalSize_tput()
                # needed for window's python in cygwin's xterm!
        if current_os == 'Linux' or current_os == 'Darwin' or current_os.startswith('CYGWIN'):
            tuple_xy = self._getTerminalSize_linux()
        if tuple_xy is None:
            tuple_xy = (80, 25)  # default value
        return tuple_xy

    # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的
    def _getTerminalSize_windows(self):
        res = None
        try:
            from ctypes import windll, create_string_buffer
            """
            STD_INPUT_HANDLE = -10  获取输入的句柄
            STD_OUTPUT_HANDLE = -11 获取输出的句柄
            STD_ERROR_HANDLE = -12  获取错误的句柄
            """
            h = windll.kernel32.GetStdHandle(-12)  # 获得输入、输出/错误的屏幕缓冲区的句柄
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        except:
            return None
        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
        else:
            return None

    # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的

    def _getTerminalSize_tput(self):
        try:
            import subprocess
            proc = subprocess.Popen(["tput", "cols"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.communicate(input=None)
            cols = int(output[0])
            proc = subprocess.Popen(["tput", "lines"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.communicate(input=None)
            rows = int(output[0])
            return (cols, rows)
        except:
            return None

    def _getTerminalSize_linux(self):
        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            except:
                return None
            return cr

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            try:
                env = os.environ
                cr = (env['LINES'], env['COLUMNS'])
            except:
                return None
        return int(cr[1]), int(cr[0])


class ErrorHandling:
    def Outlier(self, error, plugin_name):
        self.error = str(error)
        self.plugin_name = plugin_name
        if debug_mode:
            self.Process()
        else:
            pass

    def Process(self):
        if self.error.find("timed out") != -1:
            self.ErrorBanner(self.plugin_name, "connection timeout")
        elif self.error.find("Invalid URL") != -1:
            self.ErrorBanner(self.plugin_name, "prompts url")
        elif self.error.find("getaddrinfo failed") != -1:
            self.ErrorBanner(self.plugin_name, "get addr info failed")
        elif self.error.find("Invalid header") != -1:
            self.ErrorBanner(self.plugin_name, "prompts header")
        else:
            self.ErrorBanner(self.plugin_name, "unknown")

    def ErrorBanner(self, plugin_name, error):
        print("\033[31m[ X ] {} plugin {} error\033[0m".format(plugin_name, error))


class GetRootFileLocation:  # 获取当前文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            RootFileLocation = os.path.split(os.path.realpath(__file__))[0]
            return RootFileLocation
        elif system_type == "linux" or system_type == "darwin":
            RootFileLocation = os.path.split(os.path.realpath(__file__))[0]
            return RootFileLocation

class GetToolFilePath:  # 获取TOOL文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            ToolFilePath = GetRootFileLocation().Result()+"\\Tool\\"
            return ToolFilePath
        elif system_type == "linux" or system_type == "darwin":
            ToolFilePath = GetRootFileLocation().Result()+"/Tool/"
            return ToolFilePath

class GetTempFilePath:  # 获取Temp文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            TempFilePath = GetRootFileLocation().Result()+"\\Temp\\"
            return TempFilePath
        elif system_type == "linux" or system_type == "darwin":
            TempFilePath = GetRootFileLocation().Result()+"/Temp/"
            return TempFilePath

class ExecuteChildprocess:  # 执行子进程类
    def Execute(self, command: List[str]) -> None:
        self.cmd = subprocess.Popen(command, stdout=subprocess.PIPE)

    def Read(self) -> bytes:
        text = self.cmd.stdout.read()
        return text

#这个是web的类先这这边，有点小BUG
class ScanInformation:#ActiveScanList的子表，单个URL相关漏洞表,写入父表中的SID和UID,以及子表中的SSID，使他们相关连，这个就是一个关系表，关联MEDUSA表和ActiveScanList表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ScanInformation\
                            (id INTEGER PRIMARY KEY,\
                            active_scan_id TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            scan_info_id TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_init(def)", e)
    def Write(self,**kwargs)->bool:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Url=kwargs.get("url")
        ScanInfoId=kwargs.get("scan_info_id")
        Uid = kwargs.get("uid")
        ActiveScanId = kwargs.get("active_scan_id")
        Rank = kwargs.get("rank")
        Name= kwargs.get("name")
        try:
            self.cur.execute("INSERT INTO ScanInformation(active_scan_id,url,rank,scan_info_id,uid,name,creation_time)\
            VALUES (?,?,?,?,?,?,?)",(ActiveScanId,Url,Rank,ScanInfoId,Uid,Name,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_Write(def)", e)
            return False
    def Query(self,**kwargs)->str or None:#查询相关表内容

        Uid=kwargs.get("uid")
        ActiveScanId = kwargs.get("active_scan_id")
        try:
            self.cur.execute("select * from ScanInformation where uid =? and active_scan_id = ?", (Uid,ActiveScanId,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["url"] = i[2]
                JsonValues["scan_info_id"] = i[4]
                JsonValues["rank"] = i[3]
                JsonValues["name"] = i[6]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_Query(def)", e)
            return None


class SubdomainTable:  # 这是一个子域名表
    def __init__(self,Subdomain:str,url: str, **kwargs):
        try:
            self.url = str(url)  # 目标域名
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.subdomain=Subdomain#获取的子域名
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.active_scan_id=kwargs.get("ActiveScanId")# 传入的父表SID
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Subdomain\
                            (id INTEGER PRIMARY KEY,\
                            url TEXT NOT NULL,\
                            subdomain TEXT NOT NULL,\
                            timestamp TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL,\
                            uid TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Subdomain (url,subdomain,timestamp,active_scan_id,uid) \
            VALUES (?,?,?,?,?)""", (self.url, self.subdomain,self.timestamp,self.active_scan_id,self.uid,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_Write(def)", e)

class Md5Encryption:#加密类
    def __init__(self):
        self.Md5=hashlib.md5()

    def Md5Result(self,str):
        self.Md5.update(str.encode("utf8"))
        return self.Md5.hexdigest()

    def Md5GbkResult(self,str):
        self.Md5.update(str.encode("gb2312"))
        return self.Md5.hexdigest()

class GetImageFilePath:  # 获取Image文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            ImageFilePath = GetRootFileLocation().Result()+"\\Web\\Image\\"
            return ImageFilePath
        elif system_type == "linux" or system_type == "darwin":
            ImageFilePath = GetRootFileLocation().Result()+"/Web/Image/"
            return ImageFilePath

class GetJavaScriptFilePath:  # 获取JavaScript文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            JavaScriptFilePath = GetRootFileLocation().Result()+"\\Web\\CrossSiteScriptHub\\CrossSiteScriptProject\\"
            return JavaScriptFilePath
        elif system_type == "linux" or system_type == "darwin":
            JavaScriptFilePath = GetRootFileLocation().Result()+"/Web/CrossSiteScriptHub/CrossSiteScriptProject/"
            return JavaScriptFilePath

class GetCrossSiteScriptTemplateFilePath:  # 获取CrossSiteScriptTemplate文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            CrossSiteScriptTemplateFilePath = GetRootFileLocation().Result()+"\\Web\\CrossSiteScriptHub\\CrossSiteScriptTemplate\\"
            return CrossSiteScriptTemplateFilePath
        elif system_type == "linux" or system_type == "darwin":
            CrossSiteScriptTemplateFilePath = GetRootFileLocation().Result()+"/Web/CrossSiteScriptHub/CrossSiteScriptTemplate/"
            return CrossSiteScriptTemplateFilePath

class GetAnalysisFileStoragePath:  # 获取分析文件存储路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            AnalysisFileStoragePath = GetRootFileLocation().Result()+"\\Web\\ToolsUtility\\BinaryAnalysis\\AnalysisFileStorage\\"
            return AnalysisFileStoragePath
        elif system_type == "linux" or system_type == "darwin":
            AnalysisFileStoragePath = GetRootFileLocation().Result()+"/Web/ToolsUtility/BinaryAnalysis/AnalysisFileStorage/"
            return AnalysisFileStoragePath

class GetVirusFilePath:  # 获取生成好的病毒文件路径
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            VirusFilePath = GetRootFileLocation().Result()+"\\Web\\AntiAntiVirus\\VirusFile\\"
            return VirusFilePath
        elif system_type == "linux" or system_type == "darwin":
            VirusFilePath = GetRootFileLocation().Result()+"/Web/AntiAntiVirus/VirusFile/"
            return VirusFilePath

def PortReplacement(Url,Prot):#替换URL里面的端口
    try:
        Result = re.sub(r':(6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])', ":"+str(Prot), Url)
        return Result
    except Exception as e:
        ErrorLog().Write("ClassCongregation_PortReplacement(def)", e)


class GetNistDatabaseFilePath:  #  Nist数据库文件路径返回值
    def result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            NistDatabaseFilePath = GetRootFileLocation().Result() + "\\Nist.db"
            return NistDatabaseFilePath
        elif sys.platform == "linux" or sys.platform == "darwin":
            NistDatabaseFilePath = GetRootFileLocation().Result() + "/Nist.db"
            return NistDatabaseFilePath


class BinaryDataTypeConversion:#对于原始二进制数据的类型转换
    def BytesToString(self,BytesTypeBinaryData: bytes):  # 类型转换
        try:
            BinaryData = ""
            for i in BytesTypeBinaryData:
                # 如果是bytes类型的字符串，for循环会读取单个16进制然后转换成10进制
                Data = hex(i)  # 转换会16进制
                Data = Data.replace('0x', '')
                if (len(Data) == 1):
                    Data = '0' + Data  # 位数补全
                BinaryData += '\\x' + Data

            return eval(repr(BinaryData).replace('\\\\', '\\'))#先repr将字符串转为python原生字符串，然后替换双斜杠，最后eval转回正常字符串
        except Exception as e:
            ErrorLog().Write("ClassCongregation_BinaryDataTypeConversion(class)_BytesToString(def)", e)

    def StringToBytes(self,StringTypeBinaryData: str):
        try:
            BinaryData = b""
            for i in StringTypeBinaryData:
                Code = hex(ord(i))
                Code = bytes(Code.replace('0x', ''), encoding="utf-8")
                if (len(Code) == 1):
                    Code = b'0' + Code  # 位数补全
                BinaryData += b'\\x' + Code

            return eval(repr(BinaryData).replace('\\\\', '\\'))

        except Exception as e:
            ErrorLog().Write("ClassCongregation_BinaryDataTypeConversion(class)_StringToBytes(def)", e)
